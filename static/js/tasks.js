let fil = document.getElementById('fil');
let x, y, filter, filter1, tabel, tr, td, i, txtValue;
y = 0

function filtru(filter, x, z) {
  filter1 = 'xxx'
  filter2 = 'xxx'
  filter3 = 'xxx'
  filter4 = 'xxx'

  tabel = document.getElementById('tabel');
  tr = tabel.getElementsByTagName("tr");
  if(filter.textContent != undefined){
    filter = filter.textContent
  }
  fil.style.display = ""
  fil.innerHTML += `${filter}; `;
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[x];
    if (td) {
      txtValue = td.textContent || td.innerText;
     if (filter == 'custom') {
        filter = 'Open'
        filter1 = 'CMAC'
        filter2 = 'Progres'
        filter3 = 'VNET'
        filter4 = 'LNM'
      }
      if(filter == 'All'){
        z = 0
        tr[i].style.display = "";
        fil.innerHTML = `Filtru:`;
        fil.style.display = "none"
      } else{
            if (tr[i].style.display == "" || x == y){
              if (txtValue.indexOf(filter) > -1 || txtValue.indexOf(filter1) > -1 
              || txtValue.indexOf(filter2) > -1 || txtValue.indexOf(filter3) > -1 || txtValue.indexOf(filter4) > -1) {
                tr[i].style.display = "";
              } else {
                tr[i].style.display = "none";
              }}}
      
  }
}
if(z == 0 || z){addEgm(z)}
y=x
  };
  if (value){filtru(value, 10)}


function addEgm(z) {
  egm = document.getElementById('id_egm');
  li = egm.getElementsByTagName("li");
    for (var i = 0; i < li.length; i++) {
    if (li[i].value == z || z == 0){
      li[i].style.display = "";
      } else {
        li[i].style.display = "none";
      }
    }
    }
