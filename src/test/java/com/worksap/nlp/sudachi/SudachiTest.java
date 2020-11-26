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

import java.io.InputStream;
import java.io.IOException;

abstract class SudachiTest {

    Dictionary dict;
    JapaneseTokenizer tokenizer;

    void getTokenizer(String settingsFile) throws IOException {
        String path = System.getProperty("buildDirectory");
        String settings = readAllResource(settingsFile);
        dict = new DictionaryFactory().create(path, settings);
        tokenizer = (JapaneseTokenizer)dict.create();
    }

    static String readAllResource(String file) throws IOException {
        try (InputStream src = SudachiTest.class.getResourceAsStream(file)) {
            return JapaneseDictionary.readAll(src);
        }
    }
}
