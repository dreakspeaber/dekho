document.addEventListener("DOMContentLoaded", function() {
    const like = document.querySelector("#like");
    const dislike = document.querySelector("#dislike");
    const likecount = document.querySelector("#likecount");
    const dislikecount = document.querySelector("#dislikecount");

        like.onclick = function() {
         
            const request = new XMLHttpRequest();
            let path = "/" + this.dataset.id + "/likeVideo";
            var csrftoken = Cookies.get("csrftoken");
            request.open("POST", path);
            request.setRequestHeader("X-CSRFToken", csrftoken);
            request.onload = () => {
                const data = JSON.parse(request.responseText);
                console.log(data);
                if(data.error){
                    alert("error")
                }
                if (data.result === true) {
                    likecount.innerHTML = " " + data.likes;
                    dislikecount.innerHTML = " " + data.dislikes;
                }
                if (data.result === false) {
                    likecount.innerHTML = " " + data.likes;
                    dislikecount.innerHTML = " " + data.dislikes;
                    
                }
            };
            request.send();
        };
        dislike.onclick = function() {
            const request = new XMLHttpRequest();
            let path = "/" + this.dataset.id + "/dislikeVideo";
            var csrftoken = Cookies.get("csrftoken");
            request.open("POST", path);
            request.setRequestHeader("X-CSRFToken", csrftoken);
            request.onload = () => {
                const data = JSON.parse(request.responseText);
                console.log(data);
                if(data.error){
                    alert("error")
                }
                if (data.result === true) {
                    likecount.innerHTML = " " + data.likes;
                    dislikecount.innerHTML = " " + data.dislikes;
                }
                if (data.result === false) {
                    likecount.innerHTML = " " + data.likes;
                    dislikecount.innerHTML = " " + data.dislikes;
                }
            };
            request.send();
        };
   
});