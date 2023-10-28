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

const ham = document.querySelector('#js-hamburger');
const nav = document.querySelector('#js-nav');

ham.addEventListener('click', function () {

    ham.classList.toggle('active');
    nav.classList.toggle('active');

});