document.addEventListener("DOMContentLoaded", function() {
    const cols = document.querySelectorAll(".subscribechannel");
    [].forEach.call(cols, e => {
        e.onclick = function() {
            const request = new XMLHttpRequest();
            let path = "/" + this.dataset.id + "/subscribeChannel";
            var csrftoken = Cookies.get("csrftoken");
            request.open("POST", path);
            request.setRequestHeader("X-CSRFToken", csrftoken);
            request.onload = () => {
                const data = JSON.parse(request.responseText);
                console.log(data);
                if (data.result === true) {
                    e.innerHTML = "Unsubscribe";
                }
                if (data.result === false) {
                    e.innerHTML = "subscribe";
                }
            };
            request.send();
        };
    });
});