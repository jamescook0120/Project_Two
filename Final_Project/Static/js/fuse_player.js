const options = {
  isCaseSensitive: false,
  includeScore: false,
  shouldSort: true,
  includeMatches: false,
  findAllMatches: false,
  minMatchCharLength: 1,
  location: 0,
  threshold: 0.6,
  distance: 100,
  useExtendedSearch: false,
  ignoreLocation: false,
  ignoreFieldNorm: false,
 
 
  keys: ['Player', 'Rnd', 'Pick', 'Position','College'
  ]
};

const fuse = new Fuse(draft_list, options);

// Change the pattern
const pattern = "Tim"

return fuse.search(pattern)


