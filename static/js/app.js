// Select the button
var button = d3.select("#button");

// Select the form
var form = d3.select("#form-school");

// Create event handlers 
button.on("click", runEnter);
form.on("submit",runEnter);

// Complete the event handler function for the form
function runEnter() {

  // Prevent the page from refreshing
  d3.event.preventDefault();
  
  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#school-search");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  var outputValue = "Hello";

  d3.json(`/schoolsearch/${inputValue}`)
    .then(function(school_data){
    console.log("Put Me In Coach");
    outputValue = school_data
    console.log(outputValue);
  
  
    console.log(outputValue[1]);
  
    var school_info = outputValue[0];

    var attendanceInfo = outputValue[1];
    
    console.log(attendanceInfo);
    
    let years = attendanceInfo.map(a => a.year);
    let attendance =attendanceInfo.map(a => a.total_attendance);
    
    console.log(attendance);
    var data = [ 
      {
        x: years,
        y: attendance,
        type: 'bar'
      }
    ];


    var layout = {
      title: "Your School's Attendance",
      xaxis: { title: "Years"},
      yaxis: { title: "Attendance"}
    };

    // graph = document.getElementById('graphyboy');
    // Plotly.newPlot( graph, [
    // x: years,
    // y: attendance
    // ], {
    // margin: { t: 0 } } );
    Plotly.newPlot('graphyboy', data, layout);

    var tbody = d3.select("tbody");

    school_info.forEach((updateTable) => {
      var row = tbody.append("tr");
      Object.entries(updateTable).forEach(([key, value]) => {
        var cell = row.append("td");
        cell.text(value);
      });
    });
  });


  
 

  //window.location.href=`/schoolsearch/${inputValue}`

  
  
};

