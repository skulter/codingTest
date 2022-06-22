function getIdsByMessage(xml, message) {
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(xml,"text/xml");
    const messages = xmlDoc.getElementsByTagName('message');
    for(let msg of messages){
      if(msg.innerText === message) {
          msg.parentElement.id
      }
    }
  }
  
  var xmlData = 
  `<?xml version="1.0" encoding="UTF-8"?>
  <log>
    <entry id="1">
      <message>Application started</message>
    </entry>
    <entry id="2">
      <message>Application ended</message>
    </entry>
    <entry id="3">
      <message>Application ended</message>
    </entry>
  </log>`;
  
  var ids = getIdsByMessage(xmlData, "Application ended");
  console.log(ids == undefined ? ids : ids.join());