var Data;
var Inserted = 0;

function populateTable(lData) {
    Data = lData;
    let Table = document.getElementById("research-table")
    let old_tbody = document.getElementById('research-tbody')
    let new_tbody = document.createElement("tbody");
    new_tbody.setAttribute("id", "research-tbody");
    for (let rowNumber=0; rowNumber<lData.length; rowNumber++){ 
    // for (let rowNumber=0; rowNumber<20; rowNumber++){ 
        let rowData = lData[rowNumber];
        let tableRow = new_tbody.insertRow();
        let cell0 = tableRow.insertCell(0);
        cell0.innerHTML = decodeURIComponent(rowData);
        
        // let cell1 = tableRow.insertCell(1);
        // cell1.innerHTML = decodeURIComponent(rowData[1]);
        
        let button1 = document.createElement('button');
        button1.setAttribute("type", 'button');
        button1.setAttribute("class", "interested");
        button1.setAttribute("id", rowData);
        button1.setAttribute("onclick", "Mark(this)");
        button1.innerHTML = "Interested";
        let cell1 = tableRow.insertCell(1);
        cell1.appendChild(button1);

        let button2 = document.createElement('button');
        button2.setAttribute("class", "not-interested");
        button2.setAttribute("id", rowData);
        button2.setAttribute("onclick", "Mark(this)");
        button2.setAttribute('type', 'button');
        button2.innerHTML = "Not Interested";       
        let cell2 = tableRow.insertCell(2);
        cell2.appendChild(button2);

        // let button3 = document.createElement('button');
        // button3.setAttribute("class", "show-context");
        // button3.setAttribute("id", rowNumber);
        // button3.setAttribute("onclick", "ShowContext(this)");
        // button3.setAttribute('type', 'button');
        // button3.innerHTML = "Show Context";       
        // let cell3 = tableRow.insertCell(3);
        // cell3.appendChild(button3);
    }
    Table.replaceChild(new_tbody, old_tbody);
}

function ShowContext(elmnt) {
    let tbody = document.getElementById('research-tbody');
    let rowNumber = elmnt.id;
    let tableRow = tbody.insertRow(parseInt(elmnt.id) + Inserted + 1);
    let cell0 = tableRow.insertCell(0);
    cell0.setAttribute("colspan", "2");
    Inserted += 1;
    let url = 'http://www.josh-moses.com:5000/' + elmnt.className + '/' + elmnt.id;
    cell0.innerHTML = "Test"
    fetch(url)
    .then(response=>{return response.text()})
    .then(response2=>{cell0.innerHTML = response2})
    .catch(error=>console.log(error))
}

function Mark(elmnt) {
    let url = 'http://www.josh-moses.com:5000/' + elmnt.className + '/' + elmnt.id;
    fetch(url)
    .then(response=>{return response.text()})
    .then(response2=>{console.log(response2)})
    .catch(error=>console.log(error))
}
const Url = "http://www.josh-moses.com:5000/unsorted/";

fetch(Url)
.then(response=>{return response.text()})
.then(response2=>{populateTable(response2.split("\n"))})
.catch(error=>console.log(error))
