

var tbody = d3.select("tbody");

console.log(teams);

teams.forEach((updateTable) => {
    var row = tbody.append("tr");
    Object.entries(updateTable).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });