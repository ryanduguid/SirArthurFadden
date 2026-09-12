# au-tax-legislation-corpus: trace a change to its source

Synthetic example. This is a finding aid derived from the Register's EPUB reading view, not authorised legislation, tax advice or a conclusion about legal effect.

**Input:** the fabricated [source index](tests/corpus/fixtures/publication/sample-sources.json) and [reviewed observation facts](tests/corpus/fixtures/publication/sample-observation-facts-v3.json).

From a source clone, install: `python -m pip install -e .`. That puts both `python -m fadden` and the `tax-radar-au` command on the path. The builder still reads and writes beside its own stage modules, so run its stages from the checkout.

```bash
python -m fadden export_monitor_contract -- tests/corpus/fixtures/publication/sample-sources.json tests/corpus/fixtures/publication/sample-observation-facts-v3.json --out ../synthetic-monitor-example
```

**Output:** `monitor-baseline.json` and `register-observation.json` in the named output directory. The synthetic title `C2099A00001` is recorded as `SUPERSEDED`; the pair carries the evidence and source identity for review.

**Human decision:** Inspect the cited source and decide whether the apparent change affects a workpaper or workflow. This offline example makes no Register request and establishes no real legislative change.

<details>
<summary>Build the corpus, inspect contracts and check limitations</summary>

## Two related systems

The corpus builder (`python -m fadden`) produces retrieval material from Commonwealth legislation. The change-review queue (`tax-radar-au`) consumes a reviewed observation contract and raises items for a person to assess.

**Package lifecycle:** source-only. The builder is not published to PyPI; releases carry source archives, not a ready-made corpus or a builder wheel. The queue has its own package identity; this source install does not download legislation.

## Reference

- [Pipeline commands and operating boundaries](BUILD.md)
- [Synthetic review queue](RADAR.md)
- [Monitor export and recovery contract](docs/monitor-contract.md)
- [Live capture and publication evidence boundaries](docs/evidence-export.md)
- [Dated build evidence and known corrections](docs/build-evidence.md)
- [Architecture](docs/architecture.md)
- [Accuracy, scope and redistribution limits](docs/scope.md)
- [Release rules](RELEASING.md) and [contributor checks](AGENTS.md)

Live Register capture, synthetic observations and publication candidates have distinct contracts. A successful capture or export does not authorise publication.

## Source and licence

The primary source is the [Federal Register of Legislation](https://www.legislation.gov.au/). The repository contains code, not the corpus; generated output retains its own source and licence records.

Code: [MIT](LICENSE). Read the [redistribution limits](docs/scope.md#what-this-deliberately-does-not-ship) before handling generated material.

</details>
