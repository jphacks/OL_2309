var checkedCount = 0;

function ExecuteSubmit() {
    countChecked();

    if (checkedCount > 0) {
        alert('名刺を作成しました！！');
        return true;
    }
    else {
        alert("共有するSNSを選択してください．アイコンをクリックすると選択できます．");
        return false;
    }
}

function countChecked() {
    var checkboxes = document.querySelectorAll('input[type="checkbox"]');

    checkedCount = 0;

    checkboxes.forEach(function (checkbox) {
        if (checkbox.checked) {
            checkedCount++;
            console.log(checkedCount);
        }
    });
}
function selectedDesign() {
    var design1 = document.getElementById("selectSimple");
    var design2 = document.getElementById("selectCute");
    var design3 = document.getElementById("selectCat");
    var design4 = document.getElementById("selectBlock");
    var design5 = document.getElementById("selectSpace");

    if (design1.checked) {
        design2.style.visibility = "hidden";
        design3.style.visibility = "hidden";
        design4.style.visibility = "hidden";
        design5.style.visibility = "hidden";
    }
    else if (design2.checked) {
        design1.style.visibility = "hidden";
        design3.style.visibility = "hidden";
        design4.style.visibility = "hidden";
        design5.style.visibility = "hidden";
    }
    else if (design3.checked) {
        design1.style.visibility = "hidden";
        design2.style.visibility = "hidden";
        design4.style.visibility = "hidden";
        design5.style.visibility = "hidden";
    }
    else if (design4.checked) {
        design1.style.visibility = "hidden";
        design2.style.visibility = "hidden";
        design3.style.visibility = "hidden";
        design5.style.visibility = "hidden";
    }
    else {
        design1.style.visibility = "hidden";
        design2.style.visibility = "hidden";
        design3.style.visibility = "hidden";
        design4.style.visibility = "hidden";
    }
}

const ham = document.querySelector('#js-hamburger');
const nav = document.querySelector('#js-nav');

ham.addEventListener('click', function () {

    ham.classList.toggle('active');
    nav.classList.toggle('active');

});