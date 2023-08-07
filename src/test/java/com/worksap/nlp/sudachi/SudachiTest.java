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

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

abstract class SudachiTest {

    Dictionary dict;
    JapaneseTokenizer tokenizer;

    void getTokenizer(String dictName) throws IOException {
        Path basicPath = Paths.get(System.getProperty("buildDirectory"));
        Config cfg = Config.defaultConfig().systemDictionary(basicPath.resolve(dictName));
        dict = new DictionaryFactory().create(cfg);
        tokenizer = (JapaneseTokenizer)dict.create();
    }
}
