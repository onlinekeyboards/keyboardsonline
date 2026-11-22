document.addEventListener('DOMContentLoaded',function(){
 var out=document.getElementById('output');
 var dataEl=document.getElementById('kb-data');
 var shift=false;
 function updateCounts(){ if(!out) return; var t=out.value; var w=t.trim()?t.trim().split(/\s+/).length:0;
  var c=document.getElementById('counts'); if(c) c.textContent=w+' words · '+t.length+' characters · '+t.replace(/\s/g,'').length+' characters without spaces'; }
 function insertText(s){ if(!out) return; var s0=out.selectionStart||0, e=out.selectionEnd||0;
  out.value=out.value.slice(0,s0)+s+out.value.slice(e); var p=s0+s.length; out.focus(); out.setSelectionRange(p,p); updateCounts(); }
 function build(){ if(!dataEl||!out) return; var data=JSON.parse(dataEl.textContent); var kb=document.getElementById('keyboard'); if(!kb) return;
  kb.innerHTML=''; data.rows.forEach(function(row){ var r=document.createElement('div'); r.className='kb-row';
   row.forEach(function(k){ var parts=String(k).split('|'); var b=document.createElement('button'); b.type='button'; b.className='kb-key';
    b.textContent=shift&&parts[1]?parts[1]:parts[0]; b.dataset.normal=parts[0]; b.dataset.shift=parts[1]||parts[0];
    b.setAttribute('aria-label','Type '+parts[0]); b.addEventListener('click',function(){ insertText(b.dataset.shift&&shift?b.dataset.shift:b.dataset.normal); }); r.appendChild(b); });
   kb.appendChild(r); });
  var cr=document.createElement('div'); cr.className='kb-row';
  [['Shift','shift',1],['Space',' ',3],['Backspace','back',1],['Enter','enter',1]].forEach(function(x){
   var b=document.createElement('button'); b.type='button'; b.className='kb-key wide'+(x[0]==='Shift'&&shift?' shift-on':''); b.textContent=x[0];
   b.addEventListener('click',function(){ if(x[1]==='shift'){ shift=!shift; build(); } else if(x[1]==='back'){ if(out){ var s0=out.selectionStart||0,e=out.selectionEnd||0; if(s0!==e){ out.value=out.value.slice(0,s0)+out.value.slice(e); out.setSelectionRange(s0,s0);} else if(s0>0){ out.value=out.value.slice(0,s0-1)+out.value.slice(s0); out.setSelectionRange(s0-1,s0-1);} out.focus(); updateCounts(); } } else if(x[1]==='enter'){ insertText('\n'); } else { insertText(' '); } });
   cr.appendChild(b); }); kb.appendChild(cr); }
 if(out){ out.addEventListener('input',updateCounts); updateCounts(); }
 build();
 var copyBtn=document.getElementById('copy-btn'); if(copyBtn&&out) copyBtn.addEventListener('click',function(){ var done=function(){ copyBtn.textContent='Copied!'; setTimeout(function(){copyBtn.textContent='Copy text';},1500); };
  if(navigator.clipboard&&navigator.clipboard.writeText){ navigator.clipboard.writeText(out.value).then(done).catch(function(){ out.select(); document.execCommand('copy'); done(); }); } else { out.select(); document.execCommand('copy'); done(); } });
 var clearBtn=document.getElementById('clear-btn'); if(clearBtn&&out) clearBtn.addEventListener('click',function(){ out.value=''; out.focus(); updateCounts(); });
 var dlBtn=document.getElementById('download-btn'); if(dlBtn&&out) dlBtn.addEventListener('click',function(){ var blob=new Blob([out.value],{type:'text/plain;charset=utf-8'}); var a=document.createElement('a'); a.href=URL.createObjectURL(blob); a.download='keyboardsonline-text.txt'; a.click(); setTimeout(function(){URL.revokeObjectURL(a.href);},1000); });
 var selBtn=document.getElementById('select-btn'); if(selBtn&&out) selBtn.addEventListener('click',function(){ out.focus(); out.select(); });
 var search=document.getElementById('kb-search'); if(search){ search.addEventListener('input',function(){ var q=search.value.toLowerCase(); document.querySelectorAll('.kb-card').forEach(function(card){ card.style.display=card.dataset.name.toLowerCase().includes(q)?'':'none'; }); }); }
});
