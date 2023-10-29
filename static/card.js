function handleClick(logoName) {
    var result = window.confirm(logoName + 'をフォローしますか？');

    if (result) {
        console.log('フォロー申請を送信しました！');
    }
}
