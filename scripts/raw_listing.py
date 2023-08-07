import io
from typing import IO

INLINE_TAGS = {"a", "span", "i"}


def block_tag(name) -> bool:
    return name not in INLINE_TAGS


class DocumentRenderer(object):
    def __init__(self, buf: IO[str]):
        self.buf = buf
        self._indent_base = 2
        self._indent = 0
        self._in_render = False

    def _start_tag(self, name: str, attrs: dict[str, str]):
        buf = self.buf
        buf.write("<")
        buf.write(name)
        for akey, aval in attrs.items():
            buf.write(" ")
            buf.write(akey)
            buf.write("=\'")
            buf.write(aval)
            buf.write("\'")
        buf.write(">")

    def _end_tag(self, name):
        buf = self.buf
        buf.write("</")
        buf.write(name)
        buf.write(">")

    def _render_first(self, tag, args, kwargs):
        self._in_render = True
        try:
            self._render(tag, args, kwargs)
        finally:
            self._in_render = False

    def _newline(self):
        buf = self.buf
        buf.write("\n")
        for _ in range(self._indent):
            buf.write(" ")

    def _render(self, tag, args, kwargs):
        has_children = any(isinstance(x, tuple) and block_tag(x[0]) for x in args)

        self._start_tag(tag, kwargs)
        if has_children:
            self._indent += self._indent_base
        for child in args:
            if isinstance(child, tuple):
                tag_name, tag_args, tag_kwargs = child
                if has_children:
                    self._newline()
                self._render(tag_name, tag_args, tag_kwargs)
            else:
                self.buf.write(str(child))
        if has_children:
            self._indent -= self._indent_base
            self._newline()
        self._end_tag(tag)

    def render(self, structure):
        name, args, kwargs = structure
        self._render_first(name, args, kwargs)


class DocStructure(object):
    def __getattr__(self, item):
        return TagWrapper(item)


class TagWrapper(object):
    def __init__(self, name: str):
        self._name = name

    def __call__(self, *args, **kwargs):
        return self._name, args, kwargs


def gather_files(s3, bucket, prefix):
    bucket_obj = s3.Bucket(bucket)

    by_version = dict()

    for obj in bucket_obj.objects.filter(Prefix=prefix, MaxKeys=5000):
        key = obj.key
        if not key.endswith("_lex.zip"):
            continue
        key_wo_prefix = key[len(prefix) + 1:]
        version, file = key_wo_prefix.split("/", 2)
        by_version.setdefault(version, dict())[file] = key_wo_prefix

    return by_version


def render_table(data: dict[str, dict[str, str]]):
    rows = sorted(data.keys(), reverse=True)
    cols = ["small_lex.zip", "core_lex.zip", "notcore_lex.zip"]

    r = DocStructure()

    header = r.tr(
        r.td("Release"),
        *[r.td() for _ in cols]
    )

    table_rows = []

    for row in rows:
        table_row = [
            r.td(row)
        ]
        data_row = data.get(row)
        for col in cols:
            s3_key = data_row.get(col)
            value = ""
            if s3_key is not None:
                value = r.a(
                    col,
                    href=s3_key
                )
            table_row.append(
                r.td(value)
            )
        table_rows.append(
            r.tr(*table_row)
        )

    return r.table(
        r.thead(
            header,
        ),
        r.tbody(
            *table_rows
        )
    )


def compute_cols(data):
    cols = set()
    for item in data.values():
        cols.update(item)
    cols = sorted(cols)
    return cols


def render_doc(table=""):
    r = DocStructure()
    structure = r.html(
        r.head(
            r.link(rel="stylesheet", href="/css/style.css"),
            r.title("Sudachi Dictionary Sources (CSV)"),
            r.meta(name="viewport", content="width=device-width, initial-scale=1"),
            lang="en"
        ),
        r.body(
            r.h1(
                "Sudachi Dictionary Sources"
            ),
            r.p(
                "You may also need the ",
                r.a(
                    "matrix.def",
                    href="matrix.def.zip",
                ),
                " file to build the binary dictionary"
            ),
            table
        )
    )
    iobj = io.StringIO()
    iobj.write("<!doctype html>\n")
    DocumentRenderer(iobj).render(structure)

    return iobj.getvalue()


def generate_raw_listing(s3, bucket="sudachi", prefix="sudachdic-raw") -> str:
    files = gather_files(s3, bucket, prefix)
    return render_doc(render_table(files))


def _main():
    import sys
    from aws_common import CredentialCache

    s3 = CredentialCache(sys.argv[1], sys.argv[2]).session.resource("s3")
    table = generate_raw_listing(s3)
    print(render_doc(table))


if __name__ == '__main__':
    _main()
