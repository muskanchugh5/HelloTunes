var acAnimated = {Plugins: {}};
acAnimated.Plugins.AddObjects = function(element, noteSchema) {
  for (var i=0; i<=10-1; i++) { //set count in css too for number of elements
    var note = document.createElement("div");
    note.className = "note note" + String(i + 1);
    note.innerHTML = noteSchema;
    element.appendChild(note);
  }
}
acAnimated.Plugins.AddObjects(document.body.querySelector(".flying-notes"), document.body.querySelector(".note-schema").innerHTML);