# Changelog
All notable changes to **Jobtimize** will be documented in this file.

## [Unrelease](https://github.com/Lrakotoson/Jobtimize/projects)
- Adding linkedin as a data source
- Completion of missing data using text mining
- Object-Oriented Use of Jobtimize
---

## [0.0.5-alpha](https://github.com/Lrakotoson/Jobtimize/releases/tag/0.0.5-alpha.2) - 2020-09-30
### Added
- `scraper( )` function in `jobtimize.scrapers.scraper` or just `jobtimize.scraper`
- `scraper(..., maxpage)` args which give page limit for each site. *(default `maxpage=1`, it is recommended not to exceed 2 for better relevance of the search results.)*

### Changed
- Base `Jobtimize` is now `jobtimize` module
- `jobscrap( )` function is now `scraper( )`

### Deprecated
- `RotateProxies` class is deprecated and will be removed in `0.1.0`
- arg `prox` in `scraper`, `scrapIndeed`, `scrapMonster` is deprecated and will be removed in `0.1.0`
---

## [0.0.4-alpha](https://github.com/Lrakotoson/Jobtimize/releases/tag/0.0.4-alpha) - 2020-02-04
### Added
- Class `RotateProxie` in the module rotateproxie
- The `jobscrap(..., prox)` option which takes a boolean to signify the use of proxy rotation or not.

### Changed
- In the scrapmonster module, the `MonsterScrap` function takes the parameter `prox = False` by default.
- In the scrapindeed module, the `IndeedScrap` function takes the parameter `prox = False` by default.
---

## [0.0.3-alpha.1](https://github.com/Lrakotoson/Jobtimize/releases/tag/0.0.3-alpha.1) - 2020-01-30
### Added
- First alpha release
- Package avalaible on [Pypi](https://pypi.org/project/Jobtimize/) and [Anaconda](https://anaconda.org/lrakotoson/jobtimize)

---