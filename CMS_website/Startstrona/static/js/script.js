function changeBackgroundColor() {
  var color = document.getElementById("colorPicker").value;
  document.body.style.backgroundColor = color;
}

function changeTitle() {
  var newTitle = document.getElementById("titleInput").value;
  if (newTitle) {
    document.title = newTitle;
  }
}

function addTextField() {
  var div = document.createElement("div");
  div.className = 'user-text-field';
  div.setAttribute('draggable', true);
  div.addEventListener('dragstart', dragStart);
  var textField = document.createElement("textarea");
  textField.setAttribute("placeholder", "Wpisz swoją treść tutaj...");
  div.appendChild(textField);
  document.getElementById("contentArea").appendChild(div);
}

function removeTextField() {
  var fields = document.querySelectorAll('.user-text-field');
  if (fields.length > 0) {
    fields[fields.length - 1].remove();
  }
}

function toggleMenu() {
  var sidebar = document.getElementById("sidebar");
  sidebar.classList.toggle("closed");
}

let dragItem = null;

function dragStart(e) {
  dragItem = e.target;
  e.dataTransfer.effectAllowed = 'move';
  e.dataTransfer.setData('text/html', e.target.innerHTML);
}

document.getElementById("contentArea").addEventListener('dragover', (e) => {
  e.preventDefault();
});

document.getElementById("contentArea").addEventListener('drop', (e) => {
  e.preventDefault();
  if (dragItem) {
    dragItem.style.position = 'absolute';
    dragItem.style.left = e.pageX + 'px';
    dragItem.style.top = e.pageY + 'px';
  }
});


