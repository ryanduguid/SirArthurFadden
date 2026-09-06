## What it produces

Last full run, 4 August 2026:

| | |
|---|---|
| Titles | 946: 175 Acts, 675 legislative instruments, 96 notifiable instruments |
| Retrieval rows | 21,784 |
| Words | 6,041,512 |
| EPUB downloaded | 37.5 MB |
| Rates index | 4,149 entries across 286 titles |
| Download failures | 0 |
| Parse failures | 0 |

That run predates the volume-gate fix in `extract.py` and the table-stack fix
after it, and so does the `manifest_md.json` shipped beside it, so the next full
run reports more rows and words:

- the volume gate, which silently dropped five volumes of F2025L00281;
- the table stack, which let a table nested inside a cell discard the rows its
  enclosing table had already parsed. Four titles carry nested tables
  (F2005B01198, F2005L00211, F2005L01901, F2026L00716) and between them
  recovered 84 text fragments; the other 942 titles parse identically;
- the pre-section row. Text ahead of a document's first section reached the
  markdown but had no row to hold it, so it never reached `sections.jsonl`,
  which is the file retrieval reads. 511 of the 946 titles gain one
  `Introductory material` row each, carrying material such as the long title,
  the assent note and the enacting words. No title loses retrievable text;
- the pre-body table gate, which dropped a table or figure sitting between two
  pre-body paragraphs while keeping the prose either side. This changes the
  markdown for one title.

See [BUILD.md](../BUILD.md).

Layout under the corpus root:

```
epub/<register_id>.epub              the file exactly as the Register served it
markdown/<register_id>/<id>.md       full text, YAML front matter
markdown/<register_id>/sections.jsonl one row per section, ready for RAG
markdown/<register_id>/endnotes.md   amendment history, kept out of the sections
rates/rates.jsonl, rates/RATES.md    derived rates and thresholds index
sources.json, INDEX.md, README.md, LICENCE-NOTICE.md
```

Every JSONL row carries its own register id, collection, compilation number,
compilation date, section, source URL, licence and attribution, because rows
travel independently of the file they came from.
