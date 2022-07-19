var editarImg = document.querySelector(".editar-content");
var buttonFile = document.getElementById("file-preview-js");

editarImg.addEventListener("click", function(){
    buttonFile.click()
})

btnClose.addEventListener("click", function(){
    btnClose.style.display = "none"
    // output.style.display = "none"
    output.style.backgroundImage = "url('')";
    document.getElementById("file-preview-js").value = "";
})