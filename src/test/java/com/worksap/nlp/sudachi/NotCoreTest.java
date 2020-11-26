/*
 * Copyright (c) 2019 Works Applications Co., Ltd.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.worksap.nlp.sudachi;

import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.MatcherAssert.assertThat;

import java.io.IOException;
import java.util.List;

import org.junit.Before;
import org.junit.Test;

public class NotCoreTest extends SudachiTest {

    @Before
    public void setUp() throws IOException {
        getTokenizer("/sudachi_fulldict.json");
    }

    @Test
    public void splitB() {
        List<Morpheme> ms = tokenizer.tokenize("いくら丼");
        assertThat(ms.size(), is(1));
        Morpheme m = ms.get(0);
        List<Morpheme> ams = m.split(Tokenizer.SplitMode.A);
        assertThat(ams.size(), is(2));
        assertThat(ams.get(0).surface(), is("いくら"));
        assertThat(ams.get(1).surface(), is("丼"));
    }

    @Test
    public void splitC() {
        List<Morpheme> ms = tokenizer.tokenize("鹿児島中央郵便局");
        assertThat(ms.size(), is(1));
        Morpheme m = ms.get(0);
        List<Morpheme> bms = m.split(Tokenizer.SplitMode.B);
        assertThat(bms.size(), is(3));
        assertThat(bms.get(0).surface(), is("鹿児島"));
        assertThat(bms.get(1).surface(), is("中央"));
        assertThat(bms.get(2).surface(), is("郵便局"));
        List<Morpheme> ams = m.split(Tokenizer.SplitMode.A);
        assertThat(ams.size(), is(4));
        assertThat(ams.get(0).surface(), is("鹿児島"));
        assertThat(ams.get(1).surface(), is("中央"));
        assertThat(ams.get(2).surface(), is("郵便"));
        assertThat(ams.get(3).surface(), is("局"));
        List<Morpheme> ams2 = bms.get(2).split(Tokenizer.SplitMode.A);
        assertThat(ams2.size(), is(2));
        assertThat(ams2.get(0).surface(), is("郵便"));
        assertThat(ams2.get(1).surface(), is("局"));
    }

}
