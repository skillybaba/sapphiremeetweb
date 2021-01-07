var qrGenrator = (elementid,qrvalue)=>{
    console.log('qu');
    var qr =  new QRious({
        element:document.getElementById(elementid),
        size:400,
        value:qrvalue,
    });

}