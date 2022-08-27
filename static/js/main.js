
$(document).ready(function () {
  $("#sidebarCollapse").on("click", function () {
    $("#sidebar").toggleClass("active");
    $(this).toggleClass("active");
  });
});


let fil = document.getElementById('fil');


let x, y, filter, filter1, tabel, tr, td, i, txtValue;
y = 0

function filtru(filter, x) {
  filter1 = 'xxx'
  filter2 = 'xxx'
  filter3 = 'xxx'
  filter4 = 'xxx'
  tabel = document.getElementById('tabel');
  tr = tabel.getElementsByTagName("tr");
  console.log(filter.textContent)
  console.log(y)
  filter = filter.textContent
  fil.style.display = ""
  fil.innerHTML += `${filter}; `;
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[x];
    
    if (td) {
      txtValue = td.textContent || td.innerText;
      console.log(txtValue)
     if (filter == 'custom') {
        filter = 'Open'
        filter1 = 'CMAC'
        filter2 = 'Progres'
        filter3 = 'VNET'
        filter4 = 'LNM'
        
      }
      if(filter == 'All'){
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
y=x
  };





