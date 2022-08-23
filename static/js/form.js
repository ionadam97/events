var b = ''
var c = ''

const locatia = document.getElementById('id_locatia');
const list = document.getElementById('locatie');
const labelLoc = document.getElementById('Locatia');
locatia.addEventListener('change',  getLoc);
function getLoc() {
  const {value: inputVal} = locatia
  const children = Array.from(list.children)
  // Fetch matched elem
  const [matchedElem] = children.filter(({value}) => value === inputVal)
  // If element doesn't exist, no matches
  if(!matchedElem) {
    console.log('No matches found')
    return
  }
  // Do whatever
   console.log('Matched value for', matchedElem.value, 'is', matchedElem.textContent)
  a = matchedElem.value
  b = matchedElem.textContent
  addLabel()
  addEgm()
};

const egm = document.getElementById("id_egm");
const egmList = document.getElementById("adj");
const labelEgm = document.getElementById('Egm');
egm.addEventListener('change',  getEgm);
function getEgm() {
  const {value: inputVal} = egm
  const children = Array.from(egmList.children)

  // Fetch matched elem
  const [matchedElem] = children.filter(({value}) => value === inputVal)
  
  // If element doesn't exist, no matches
  if(!matchedElem) {
    console.log('No matches found')
    return
  }
  // Do whatever
   console.log('Matched value for', matchedElem.value, 'is', matchedElem.textContent)
  a = matchedElem.value
  c = matchedElem.textContent

  addLabel()

};

console.log(data)
function addEgm() {
    egmList.innerHTML = `<option value=""></option>`;
    for (var i = 0; i < data.length; i++) {
            if (data[i]['locatia_id'] == a ){
                egmList.innerHTML += `<option value="${data[i]['id']}">${data[i]['serie']}</option>`;

            }
    }
    }

    getLoc()
    getEgm()
    
function addLabel(){
    labelLoc.innerHTML = `<h5>${b}</h5>`;
    labelEgm.innerHTML = `<h5>${c}</h5>`;
}

            
