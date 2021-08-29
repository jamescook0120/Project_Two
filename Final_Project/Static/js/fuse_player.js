// var button = d3.select("#button");

// var form = d3.select("#form-search");

// button.on("click", runEnter);
// form.on("submit", runEnter);

const options = {
  isCaseSensitive: false,
  includeScore: false,
  shouldSort: true,
  includeMatches: false,
  findAllMatches: false,
  minMatchCharLength: 6,
  location: 0,
  threshold: 0.2,
  distance: 100,
  useExtendedSearch: false,
  ignoreLocation: false,
  ignoreFieldNorm: false,


  keys: ['Player', 'Position', 'College'
  ]
};

var tbody = d3.select("tbody");

player_list.forEach((updateTable) => {
  var row = tbody.append("tr");
  Object.entries(updateTable).forEach(([key, value]) => {
    var cell = row.append("td");
    cell.text(value);
  });
});

const fuse = new Fuse(player_list, options);

function runEnter(selectedPlayerName) {
  console.log(selectedPlayerName)
  // d3.event.preventDefault();

  // var inputElement = d3.select("#searchbar");

  // var inputValue = inputElement.property("value");

  // console.log(inputValue);

  var searchResults = fuse.search(`${selectedPlayerName}`);
  var parsedSearchResults = [];   
  searchResults.forEach(result=>{
    console.log(result["item"])
    parsedSearchResults.push({
      "Rnd": result["item"]["Rnd"],
      "Pick": result["item"]["Pick"],
      "Tm": result["item"]["Tm"],
      "Player": result["item"]["Player"],
      "Pos": result["item"]["Pos"],
      "Age": result["item"]["Age"],
      "To": result["item"]["To"],
      "AP1": result["item"]["AP1"],
      "PB": result["item"]["PB"],
      "St": result["item"]["St"],
      "CarAV": result["item"]["CarAV"],
      "DrAV": result["item"]["DrAV"],
      "G": result["item"]["G"],
      "Cmp": result["item"]["Cmp"],
      "Att": result["item"]["Att"],
      "Yds": result["item"]["Yds"],
      "TD": result["item"]["TD"],
      "Int": result["item"]["Int"],
      "Att__1": result["item"]["Att__1"],
      "Yds__1": result["item"]["Yds__1"],
      "TD__1": result["item"]["TD__1"],
      "Rec": result["item"]["Rec"],
      "Yds__2": result["item"]["Yds__2"],
      "TD__2": result["item"]["TD__2"],
      "Solo": result["item"]["Solo"],
      "Int__1": result["item"]["Int__1"],
      "Sk": result["item"]["Sk"],
      "College": result["item"]["College"]
    })
  })

  console.log(searchResults);
  tbody.html("")
  parsedSearchResults.forEach((updateTable) => {
    var row = tbody.append("tr");
    Object.entries(updateTable).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });
}
