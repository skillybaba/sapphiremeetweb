var firebaseConfig = {
    apiKey: "AIzaSyD459mLh3V-U83_cD2ZgM4herSAq76CAHY",
    authDomain: "sapphire-meet.firebaseapp.com",
    databaseURL: "https://sapphire-meet.firebaseio.com",
    projectId: "sapphire-meet",
    storageBucket: "sapphire-meet.appspot.com",
    messagingSenderId: "414973538233",
    appId: "1:414973538233:web:387f730b004839c2369068",
    measurementId: "G-7ZBSX6GSDT"
};

firebase.initializeApp(firebaseConfig);
var main = async(docid) => {
    console.log(docid);
    await user(docid);


};

function updateScroll() {
    var element = document.getElementById("chatmess");
    element.scrollTop = element.scrollHeight;
}
var globaladd = () => {};
var first = async(docid, number) => {
    // console.log(4);

    // var firestore = firebase.firestore();
    // var doc = firestore.doc(docid);
    // var docdata = await doc.get();
    // var finalchat = '';

    // var data = docdata.data();
    // var message = data[number]['message'];
    // console.log(message);

    // for (let i in message) {

    //     if (message[i]['val'][3] == data['name']) {

    //         finalchat = finalchat + sender(message[i]['val'][0]);
    //     } else {

    //         finalchat = finalchat + recevermsg(message[i]['val'][0]);
    //     }


    // }
    document.getElementById('send').removeEventListener('click', globaladd);
    globaladd = () => {

        addmessage(docid, number);
    };
    document.getElementById('chatmess').innerHTML = finalchat;
    chatmessage(docid, number,true);

    document.getElementById('send').addEventListener('click', globaladd);

};
var chattile = (name, docid, number, avtar = 'https://static.thenounproject.com/png/503257-200.png') => {
    var st = ` <div class="row sideBar-body"  id  = ${number}>
    <div class="col-sm-3 col-xs-3 sideBar-avatar">
        <div class="avatar-icon">
            <img src="${avtar}">
        </div>
    </div>
    <div class="col-sm-9 col-xs-9 sideBar-main" >
        <div class="row">
            <div class="col-sm-8 col-xs-8 sideBar-name">
                <span class="name-meta">${name}
</span>
            </div>
            <div class="col-sm-4 col-xs-4 pull-right sideBar-time">
                <span class="time-meta pull-right">18:18
</span>
            </div>
        </div>
    </div>
</div>
`;

    return st;
}
var recevermsg = (text, img = 'null') => {
    return ` <div class="row message-body">
    <div class="col-sm-12 message-main-receiver">
        <div class="receiver">
            <div class="message-text">
            ${text}
            <img src="${img!='null'?img:''}" >
            </div>
            <span class="message-time pull-right">
Sun
</span>
        </div>
    </div>
</div>`;
};
var sender = (text, img = 'null') => {
    return `<div class="row message-body">
    <div class="col-sm-12 message-main-sender">
        <div class="sender">
            <div class="message-text">
            ${text}
            <img src="${img!='null'?img:''}" >
            </div>
            <span class="message-time pull-right">
Sun
</span>
        </div>
    </div>
</div>`;
};
var finalchat = '';
var chatmessage = async(docid, number,newglobal) => {
    if(newglobal)
    finalchat="";
    var firestore = firebase.firestore();
    var col = firestore.doc(docid).collection(number);
    var doc = firestore.doc(docid);

    doc = await doc.get();
        var data1 = doc.data();
       
            
    col.onSnapshot((snapshot) => {
        snapshot.docChanges().forEach(element => {
           var data= element.doc.data();
           if(data['user']['name']==data1['name'])
           {
            finalchat=finalchat+sender(data['text']);
           }
          else{
              finalchat=finalchat+recevermsg(data['text']);
          }
        });
        document.getElementById('chatmess').innerHTML = finalchat;
        updateScroll();
    });
        
       

};

var addmessage = async(docid, number) => {
    var firestore = firebase.firestore();
    var doc = firestore.doc(docid);
    var docdata = await doc.get();
    var data = docdata.data();
    var col1 = firestore.doc(docid).collection(number);
    var col2 = firestore.doc(data[number]['docid']).collection(data['number']);
    col1.add({
        image:null,
        text:document.getElementById('comment').value,
        time:firebase.firestore.Timestamp.fromDate(new Date()),
        user:{
            avatar:data['avatar']??null,
            docid:docid,
            name:data['name'],
        },
        video:null,
    });
    col2.add({
        image:null,
        text:document.getElementById('comment').value,
        time:firebase.firestore.Timestamp.fromDate(new Date()),
        user:{
            avatar:data['avatar']??null,
            docid:docid,
            name:data['name'],
        },
        video:null,
    });
   
 
    document.getElementById('comment').value = "";

    function updateScroll() {
        var element = document.getElementById("chatmess");
        element.scrollTop = element.scrollHeight;
    }
    updateScroll();

};
var user = async(docid) => {


    var firestore = firebase.firestore();
    var doc = firestore.doc(docid);
    console.log(docid);
    // var docdata = await doc.get();
    // var data = docdata.data();
    doc.onSnapshot(async(doc) => {
        document.getElementById('ownavtar').innerHTML = doc.data()['DP'] != null ? `<img src = "${doc.data()['DP']}" >` : `<img src = "https://static.thenounproject.com/png/503257-200.png" >`;
        var finalchat = '';
        var data = doc.data();
        var keys = Object.keys(data);

        for (let i in keys) {
            if ((keys[i] != 'name') &&
                (keys[i] != 'number') &&
                (keys[i] != 'DP') &&
                (keys[i] != 'calling') &&
                (keys[i] != 'receving') &&
                (keys[i] != 'connected') &&
                (keys[i] != 'caller') &&
                (keys[i] != 'channelid') &&
                (keys[i] != 'callhis') &&
                (keys[i] != 'downloadablelink') &&
                (keys[i] != 'status') &&
                (keys[i] != 'time')&&
                (data[keys[i]]!=null)
                ) {
                
                
                finalchat = finalchat + chattile(data[keys[i]]['name'], docid, keys[i], data[keys[i]]['avatar'] != null ?data[keys[i]]['avatar'] : 'https://static.thenounproject.com/png/503257-200.png');

            }
        }
        console.log('done');
        document.getElementById('chattile').innerHTML = finalchat;
        for (let i in keys) {
            if ((keys[i] != 'name') &&
                (keys[i] != 'number') &&
                (keys[i] != 'DP') &&
                (keys[i] != 'calling') &&
                (keys[i] != 'receving') &&
                (keys[i] != 'connected') &&
                (keys[i] != 'caller') &&
                (keys[i] != 'channelid') &&
                (keys[i] != 'callhis') &&
                (keys[i] != 'downloadablelink') &&
                (keys[i] != 'status') &&
                (keys[i] != 'time')&&
                (data[keys[i]]!=null)
                ) {
               
                document.getElementById(keys[i]).addEventListener('click', async() => {
                    await first(docid, keys[i]);
                    document.getElementById('avatar').innerHTML = data[keys[i]]['avtar'] != null ? ` <img src = "${data[keys[i]]['avtar']}" > ` : ` <img src = "https://static.thenounproject.com/png/503257-200.png" > `
                    document.getElementById('headname').innerHTML = data[keys[i]]['name'];

                    function updateScroll() {
                        var element = document.getElementById("chatmess");
                        element.scrollTop = element.scrollHeight;
                    }
                    updateScroll();
                });

            }
        }
    });



}