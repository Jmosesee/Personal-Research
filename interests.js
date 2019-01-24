var Data;

function populateTable(lData) {
    Data = lData;
    let Table = document.getElementById("interests-table")
    let old_tbody = document.getElementById('interests-tbody')
    let new_tbody = document.createElement("tbody");
    new_tbody.setAttribute("id", "interests-tbody");
    for (let rowNumber=0; rowNumber<lData.length; rowNumber++){ 
        let rowData = lData[rowNumber].split(",");
        let tableRow = new_tbody.insertRow();
        let cell0 = tableRow.insertCell(0);
        cell0.innerHTML = rowData[0];
        let button1 = document.createElement('button');
        button1.setAttribute("class", "not-interested");
        button1.setAttribute("id", rowData[0]);
        button1.setAttribute("onclick", "Mark(this)");
        button1.setAttribute('type', 'button');
        button1.innerHTML = "Not Interested";
        let cell1 = tableRow.insertCell(1);
        cell1.appendChild(button1);
    }
    Table.replaceChild(new_tbody, old_tbody);
}

function Mark(elmnt) {
    let url = 'http://www.josh-moses.com:5000/' + elmnt.className + '/' + elmnt.id;
    fetch(url)
    .then(response=>{return response.text()})
    .then(response2=>{console.log(response2)})
    .catch(error=>console.log(error))
}
const Url = "http://www.josh-moses.com:5000/interests/";

fetch(Url)
.then(response=>{return response.text()})
.then(response2=>{populateTable(response2.split("\n"))})
.catch(error=>console.log(error))
