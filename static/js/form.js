var idLocatie;
const locatia = document.getElementById("id_locatia");
const egm = document.getElementById("id_egm");

locatia.addEventListener("change", getLocatia);

function getLocatia() {
  idLocatie = locatia.options[locatia.selectedIndex].value;
  addEgm();
}

function addEgm() {
  egm.innerHTML = `<option value="">----------</option>`;
  for (var i = 0; i < data.length; i++) {
    if (data[i]["locatia_id"] == idLocatie) {
      egm.innerHTML += `<option value="${data[i]["id"]}">${data[i]["serie"]}</option>`;
    }
  }
}
