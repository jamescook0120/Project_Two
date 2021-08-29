var button = d3.select("#button");

var form = d3.select("#form-search");

button.on("click", runEnter);
form.on("submit",runEnter);

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
 
 
  keys: ['Player', 'Position','College'
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

function runEnter(){

  d3.event.preventDefault();
  
  var inputElement = d3.select("#searchbar"); 

  var inputValue = inputElement.property("value");
  
  // console.log(inputValue);

  var searchResult = fuse.search(`${inputValue}`);
  
  console.log(searchResult);
  
  searchResult.forEach((updateTable) => {
    var row = tbody.append("tr");
    Object.entries(updateTable).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
});
}







// Change the pattern
// const pattern = "Tim"

// return fuse.search(pattern)


