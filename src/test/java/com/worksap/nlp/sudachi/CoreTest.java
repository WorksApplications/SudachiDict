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

import static org.hamcrest.CoreMatchers.equalTo;
import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.CoreMatchers.not;
import static org.hamcrest.MatcherAssert.assertThat;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;

import org.junit.Before;
import org.junit.Test;

public class CoreTest extends SudachiTest {

    @Before
    public void setUp() throws IOException {
        getTokenizer("/sudachi.json");
    }

    @Test
    public void partOfSpeech() {
        List<Morpheme> ms = tokenizer.tokenize("京都");
        assertThat(ms.size(), is(1));
        Morpheme m = ms.get(0);
        List<String> pos = m.partOfSpeech();

        assertThat(pos, is(equalTo(Arrays.asList(new String[] {"名詞", "固有名詞", "地名", "一般", "*", "*"}))));
    }

    @Test
    public void splitB() {
        List<Morpheme> ms = tokenizer.tokenize("東京都");
        assertThat(ms.size(), is(1));
        Morpheme m = ms.get(0);
        List<Morpheme> ams = m.split(Tokenizer.SplitMode.A);
        assertThat(ams.size(), is(2));
        assertThat(ams.get(0).surface(), is("東京"));
        assertThat(ams.get(1).surface(), is("都"));
    }

    @Test
    public void splitC() {
        List<Morpheme> ms = tokenizer.tokenize("黒部市前沢");
        assertThat(ms.size(), is(1));
        Morpheme m = ms.get(0);
        List<Morpheme> bms = m.split(Tokenizer.SplitMode.B);
        assertThat(bms.size(), is(2));
        assertThat(bms.get(0).surface(), is("黒部市"));
        assertThat(bms.get(1).surface(), is("前沢"));
        List<Morpheme> ams = m.split(Tokenizer.SplitMode.A);
        assertThat(ams.size(), is(3));
        assertThat(ams.get(0).surface(), is("黒部"));
        assertThat(ams.get(1).surface(), is("市"));
        assertThat(ams.get(2).surface(), is("前沢"));
        List<Morpheme> ams2 = bms.get(0).split(Tokenizer.SplitMode.A);
        assertThat(ams2.size(), is(2));
        assertThat(ams2.get(0).surface(), is("黒部"));
        assertThat(ams2.get(1).surface(), is("市"));
    }

    @Test
    public void splitInNotCore() {
        List<Morpheme> ms = tokenizer.tokenize(Tokenizer.SplitMode.C, "ありあけタコ街道");
        assertThat(ms.size(), is(not((1))));
    }

}
