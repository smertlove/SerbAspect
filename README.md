# SerbAspect

Serbian grammar aspect prediction experiments.

## Data preparation

The Serbian Universal Dependencies (UD) train subset [1] was used as the main and only source of marked down data. The data was parsed into NLTK DependencyGraph structures [2], and verb lemmas were mapped on their corresponding dataset entries. To prevent data undersampling and to ensure adequate representation, the dataset was then filtered to retain only lemmas with at least 5 distinct occurrences. Entries exhibiting identical forms of the target verb lemma were also removed. Following these preprocessing steps, we have ended up with 4959 rows of data.

The grammar aspect of a verb, which is our target variable, is not present in Serbian UD dataset. The manual annotation process was conducted using Serbian verb government dictionary [3]. For the biaspectual verbs we have also tried aspectual disambiguation assignment, although it was challenging and probably useless as even within contextual information they tend to still be rock solid ambiguous.

Finally, various features were extracted from the DependencyGraph structures and appended to the dataset. These features were selected for their potential to improve the performance of classical ML models, like Decision Trees or Gradient Boostings. The final dataset structure can be examined below:

- lemma — lemma of a verb, latin lowercased
- word — form of a verb, original case preserved
- aspect — grammar aspect of a lemma (`perf`, `imp` or `both`)
- disambig — grammar aspect of a verb form in context (`perf`, `imp` or `both`)
- db_id — UD_Serbian-SET sent_id
- text — raw text context
- Gender — grammatical gender of a verb (`Fem`, `Masc`, `Neut` or `nan`)
- Mood — grammatical mood of a verb (`Ind`, `Imp` or `nan`)
- Number — grammatical number of a verb (`Sing`, `Plur` or `nan`)
- POS — part of speech of a verb (`VERB` or `nan`)
- Person — grammatical person of a verb (1, 2, 3 or `nan`)
- Tense — grammatical tense of a verb (`Pres`, `Past`, `Fut` or `nan`)
- VerbForm — grammatical form of a verb (`Fin`, `Part`, `Inf` or `nan`)
- Voice — grammatical voice of a verb (`Act` or `nan`)
- l_tok_3 — 3rd token on the left of the target verb (or `[PAD]`)
- l_tok_2 — 2nd token on the left of the target verb (or `[PAD]`)
- l_tok_1 — 1st token on the left of the target verb (or `[PAD]`)
- r_tok_1 — 1st token on the right of the target verb (or `[PAD]`)
- r_tok_2 — 2nd token on the right of the target verb (or `[PAD]`)
- r_tok_3 — 3rd token on the right of the target verb (or `[PAD]`)
- l_gr_1 — 3rd left grapheme of the target verb (or `[PAD]`)
- l_gr_2 — 2nd left grapheme of the target verb (or `[PAD]`)
- l_gr_3 — 1st left grapheme of the target verb (or `[PAD]`)
- r_gr_1 — 1st right grapheme of the target verb (or `[PAD]`)
- r_gr_2 — 2nd right grapheme of the target verb (or `[PAD]`)
- r_gr_3 — 3rd right grapheme of the target verb (or `[PAD]`)
- nsubj — a list of frequent nominal subjects of the verb (>5 occurances)
- nsubj_count — number of nominal subjects of the verb
- obj — a list of frequent direct objects (>5 occurances)
- obj_count — number of direct objects
- obl — a list of frequent oblique nominals of the verb (>5 occurances)
- obl_count — number of oblique nominals of the verb
- advmod — a list of frequent adverbal modifiers of the verb (>5 occurances)
- advmod_count — number of adverbal modifiers of the verb

## References

1) [UD_Serbian-SET](https://github.com/UniversalDependencies/UD_Serbian-SET/tree/master)
2) [nltk.parse.dependencygraph module](https://www.nltk.org/api/nltk.parse.dependencygraph.html)
3) [Rečnik glagola: Sa dopunama (Serbo-Croatian Edition)](https://isbndb.com/book/9788617011503)
