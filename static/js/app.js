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
  d3.event.preventDefault(
  
  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#school-search");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);

  var outputValue = {a:b};

  d3.json(`/schoolsearch/${inputValue}`)
    .then(function(school_data){
    console.log("Put Me In Coach");
    outputValue = school_data;

  });

  console.log(outputValue);
  )
};
