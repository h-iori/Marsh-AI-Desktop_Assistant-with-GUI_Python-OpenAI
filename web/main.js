window.onbeforeunload = function () {
    eel.exit_program(); // Call Python function to exit program
};


// $(document).ready(function () {
//     $('.marshname').textillate({
//         loop: true,
//         sync: true,
//         in:{
//             effect: "fadeInLeft",
//         },
//         out:{
//             effect: "fadeOutRight",
//         }            
//     })
// });


$(document).ready(function () {
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "fadeInUp",
        },
        out:{
            effect: "fadeOutRight",
        }            
    })
});




function toggleSidebar() {
    var sidebar = document.getElementById('sidebar');
    if (sidebar.style.left === "0px") {
        sidebar.style.left = "-200px";
    } else {
        sidebar.style.left = "0px";
    }
}
// siri wave
var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 640,
    height: 200,
    style: "ios9",
    amplitude: 4,
    frequency: 1.5,
    speed: 0.2,
    autostart: false,
  });

// Function to start the Siri wave
function startSiriWave() {
    eel.start_assistant();
    siriWave.start();
}

// Function to show the popup card
function showPopupCard() {
    var popupCard = document.getElementById('popupCardapi');
    popupCard.style.display = 'block';
}

// Function to hide the popup card
function hidePopupCard() {
    var popupCard = document.getElementById('popupCardapi');
    popupCard.style.display = 'none';
}
function showapifile() {
    eel.openapi();
}

// Function to save the input
function saveInput() {
    var inputText = document.getElementById('inputText').value;
    eel.saveTextToFile(inputText);

}

// Function to show the email popup card
function showPopupCardemail() {
    var emailpopupCard = document.getElementById('popupCardemail');
    emailpopupCard.style.display = 'block';
}

// Function to hide the email popup card
function hidePopupCardemail() {
    var emailpopupCard = document.getElementById('popupCardemail');
    emailpopupCard.style.display = 'none';
}

function showemailfile() {
    eel.openemail();
}

// Function to save the input
function emailsaveInput() {
    var inputTextname = document.getElementById('inputTextn').value;
    var inputTextemail = document.getElementById('inputTexte').value;
    var combineddata = inputTextname + ',' + inputTextemail;
    eel.saveemailToFile(combineddata);

}

// Function to show the chat data popup card
function showPopupCardchatdata() {
    var chatdatapopupCard = document.getElementById('popupCardchatdata');
    chatdatapopupCard.style.display = 'block';
}

function showchatfile() {
    eel.openchat();
}
// Function to hide the chat data popup card
function hidePopupCardchatdata() {
    var chatdatapopupCard = document.getElementById('popupCardchatdata');
    chatdatapopupCard.style.display = 'none';
}

// Function to save the input
function chatdatasaveInput() {
    var inputTextqn = document.getElementById('inputTextqn').value;
    var inputTexteans = document.getElementById('inputTexteans').value;
    eel.savechatToFile(inputTextqn, inputTexteans);

}



// Function to show the email credentials  popup card
function showPopupCardcred() {
    var credpopupCard = document.getElementById('popupCardemailcred');
    credpopupCard.style.display = 'block';
}

function showcredfile() {
    eel.opencred();
}
// Function to hide the email popup card
function hidePopupCardcred() {
    var credpopupCard = document.getElementById('popupCardemailcred');
    credpopupCard.style.display = 'none';
}

function credsaveInput() {
    var inputTextem = document.getElementById('inputTextem').value;
    var inputTextpass = document.getElementById('inputTextpass').value;
    eel.savecredToFile(inputTextem,inputTextpass);
    hidePopupCardcred();

}
