var ob;function pb(h){var f=0;return function(){return f<h.length?{done:!1,value:h[f++]}:{done:!0}}}function qb(h){var f="undefined"!=typeof Symbol&&Symbol.iterator&&h[Symbol.iterator];return f?f.call(h):{next:pb(h)}}var dd="undefined"!=typeof window&&window===this?this:"undefined"!=typeof global&&null!=global?global:this,Fd="function"==typeof Object.defineProperties?Object.defineProperty:function(h,f,Ka){h!=Array.prototype&&h!=Object.prototype&&(h[f]=Ka.value)};
function Gd(h,f){if(f){var Ka=dd;h=h.split(".");for(var Za=0;Za<h.length-1;Za++){var bb=h[Za];bb in Ka||(Ka[bb]={});Ka=Ka[bb]}h=h[h.length-1];Za=Ka[h];f=f(Za);f!=Za&&null!=f&&Fd(Ka,h,{configurable:!0,writable:!0,value:f})}}
Gd("Promise",function(h){function f(f){this.MQf=0;this.Cug=void 0;this.Qie=[];var h=this.slg();try{f(h.resolve,h.reject)}catch(Tb){h.reject(Tb)}}function Ka(){this.FAd=null}function Za(h){return h instanceof f?h:new f(function(f){f(h)})}if(h)return h;Ka.prototype.nJg=function(f){if(null==this.FAd){this.FAd=[];var h=this;this.oJg(function(){h.Ihh()})}this.FAd.push(f)};var bb=dd.setTimeout;Ka.prototype.oJg=function(f){bb(f,0)};Ka.prototype.Ihh=function(){for(;this.FAd&&this.FAd.length;){var f=this.FAd;
this.FAd=[];for(var h=0;h<f.length;++h){var Ka=f[h];f[h]=null;try{Ka()}catch(jb){this.Heh(jb)}}}this.FAd=null};Ka.prototype.Heh=function(f){this.oJg(function(){throw f;})};f.prototype.slg=function(){function f(f){return function(z){Ka||(Ka=!0,f.call(h,z))}}var h=this,Ka=!1;return{resolve:f(this.Cph),reject:f(this.oug)}};f.prototype.Cph=function(h){if(h===this)this.oug(new TypeError("A Promise cannot resolve to itself"));else if(h instanceof f)this.Aqh(h);else{a:switch(typeof h){case "object":var z=
null!=h;break a;case "function":z=!0;break a;default:z=!1}z?this.Bph(h):this.dNg(h)}};f.prototype.Bph=function(f){var h=void 0;try{h=f.then}catch(Tb){this.oug(Tb);return}"function"==typeof h?this.Bqh(h,f):this.dNg(f)};f.prototype.oug=function(f){this.vWg(2,f)};f.prototype.dNg=function(f){this.vWg(1,f)};f.prototype.vWg=function(f,h){if(0!=this.MQf)throw Error("Cannot settle("+f+", "+h+"): Promise already settled in state"+this.MQf);this.MQf=f;this.Cug=h;this.Jhh()};f.prototype.Jhh=function(){if(null!=
this.Qie){for(var f=0;f<this.Qie.length;++f)gb.nJg(this.Qie[f]);this.Qie=null}};var gb=new Ka;f.prototype.Aqh=function(f){var h=this.slg();f.cZf(h.resolve,h.reject)};f.prototype.Bqh=function(f,h){var z=this.slg();try{f.call(h,z.resolve,z.reject)}catch(jb){z.reject(jb)}};f.prototype.then=function(h,Ka){function z(f,h){return"function"==typeof f?function(h){try{gb(f(h))}catch(hc){Ma(hc)}}:h}var gb,Ma,bb=new f(function(f,h){gb=f;Ma=h});this.cZf(z(h,gb),z(Ka,Ma));return bb};f.prototype.catch=function(f){return this.then(void 0,
f)};f.prototype.cZf=function(f,h){function z(){switch(Ka.MQf){case 1:f(Ka.Cug);break;case 2:h(Ka.Cug);break;default:throw Error("Unexpected state: "+Ka.MQf);}}var Ka=this;null==this.Qie?gb.nJg(z):this.Qie.push(z)};f.resolve=Za;f.reject=function(h){return new f(function(f,z){z(h)})};f.race=function(h){return new f(function(f,z){for(var Ka=qb(h),Ma=Ka.next();!Ma.done;Ma=Ka.next())Za(Ma.value).cZf(f,z)})};f.all=function(h){var z=qb(h),Ka=z.next();return Ka.done?Za([]):new f(function(f,h){function Ma(h){return function(z){Ta[h]=
z;gb--;0==gb&&f(Ta)}}var Ta=[],gb=0;do Ta.push(void 0),gb++,Za(Ka.value).cZf(Ma(Ta.length-1),h),Ka=z.next();while(!Ka.done)})};return f});Gd("Array.prototype.fill",function(h){return h?h:function(f,h,Za){var Ka=this.length||0;0>h&&(h=Math.max(0,Ka+h));if(null==Za||Za>Ka)Za=Ka;Za=Number(Za);0>Za&&(Za=Math.max(0,Ka+Za));for(h=Number(h||0);h<Za;h++)this[h]=f;return this}});
function Hd(h,f,Ka){if(null==h)throw new TypeError("The 'this' value for String.prototype."+Ka+" must not be null or undefined");if(f instanceof RegExp)throw new TypeError("First argument to String.prototype."+Ka+" must not be a regular expression");return h+""}Gd("String.prototype.repeat",function(h){return h?h:function(f){var h=Hd(this,null,"repeat");if(0>f||1342177279<f)throw new RangeError("Invalid count value");f|=0;for(var Za="";f;)if(f&1&&(Za+=h),f>>>=1)h+=h;return Za}});
Gd("Number.isFinite",function(h){return h?h:function(f){return"number"!==typeof f?!1:!isNaN(f)&&Infinity!==f&&-Infinity!==f}});Gd("Number.isInteger",function(h){return h?h:function(f){return Number.isFinite(f)?f===Math.floor(f):!1}});Gd("String.prototype.endsWith",function(h){return h?h:function(f,h){var Ka=Hd(this,f,"endsWith");f+="";void 0===h&&(h=Ka.length);h=Math.max(0,Math.min(h|0,Ka.length));for(var bb=f.length;0<bb&&0<h;)if(Ka[--h]!=f[--bb])return!1;return 0>=bb}});
Gd("String.prototype.padStart",function(h){return h?h:function(f,h){var Ka=Hd(this,null,"padStart");f-=Ka.length;h=void 0!==h?String(h):" ";return(0<f&&h?h.repeat(Math.ceil(f/h.length)).substring(0,f):"")+Ka}});function Be(){Be=function(){};dd.Symbol||(dd.Symbol=De)}function Ee(h,f){this.kYg=h;Fd(this,"description",{configurable:!0,writable:!0,value:f})}Ee.prototype.toString=function(){return this.kYg};
var De=function(){function h(Ka){if(this instanceof h)throw new TypeError("Symbol is not a constructor");return new Ee("jscomp_symbol_"+(Ka||"")+"_"+f++,Ka)}var f=0;return h}();function Ng(){Be();var h=dd.Symbol.iterator;h||(h=dd.Symbol.iterator=dd.Symbol("Symbol.iterator"));"function"!=typeof Array.prototype[h]&&Fd(Array.prototype,h,{configurable:!0,writable:!0,value:function(){return Kh(pb(this))}});Ng=function(){}}
function Kh(h){Ng();h={next:h};h[dd.Symbol.iterator]=function(){return this};return h}function qm(h,f){Ng();h instanceof String&&(h+="");var Ka=0,Za={next:function(){if(Ka<h.length){var bb=Ka++;return{value:f(bb,h[bb]),done:!1}}Za.next=function(){return{done:!0,value:void 0}};return Za.next()}};Za[Symbol.iterator]=function(){return Za};return Za}Gd("Array.prototype.values",function(h){return h?h:function(){return qm(this,function(f,h){return h})}});
Gd("Math.sign",function(h){return h?h:function(f){f=Number(f);return 0===f||isNaN(f)?f:0<f?1:-1}});Gd("Array.prototype.keys",function(h){return h?h:function(){return qm(this,function(f){return f})}});function Sm(h,f){return Object.prototype.hasOwnProperty.call(h,f)}
Gd("WeakMap",function(h){function f(f){this.aCf=(z+=Math.random()+1).toString();if(f){f=qb(f);for(var h;!(h=f.next()).done;)h=h.value,this.set(h[0],h[1])}}function Ka(){}function Za(f){Sm(f,gb)||Fd(f,gb,{value:new Ka})}function bb(f){var h=Object[f];h&&(Object[f]=function(f){if(f instanceof Ka)return f;Za(f);return h(f)})}if(function(){if(!h||!Object.seal)return!1;try{var f=Object.seal({}),z=Object.seal({}),Ka=new h([[f,2],[z,3]]);if(2!=Ka.get(f)||3!=Ka.get(z))return!1;Ka.delete(f);Ka.set(z,4);return!Ka.has(f)&&
4==Ka.get(z)}catch(Ma){return!1}}())return h;var gb="$jscomp_hidden_"+Math.random();bb("freeze");bb("preventExtensions");bb("seal");var z=0;f.prototype.set=function(f,h){Za(f);if(!Sm(f,gb))throw Error("WeakMap key fail: "+f);f[gb][this.aCf]=h;return this};f.prototype.get=function(f){return Sm(f,gb)?f[gb][this.aCf]:void 0};f.prototype.has=function(f){return Sm(f,gb)&&Sm(f[gb],this.aCf)};f.prototype.delete=function(f){return Sm(f,gb)&&Sm(f[gb],this.aCf)?delete f[gb][this.aCf]:!1};return f});
Gd("Map",function(h){function f(){var f={};return f.previous=f.next=f.head=f}function Ka(f,h){var z=f.b4c;return Kh(function(){if(z){for(;z.head!=f.b4c;)z=z.previous;for(;z.next!=z.head;)return z=z.next,{done:!1,value:h(z)};z=null}return{done:!0,value:void 0}})}function Za(f,h){var Ka=h&&typeof h;"object"==Ka||"function"==Ka?gb.has(h)?Ka=gb.get(h):(Ka=""+ ++z,gb.set(h,Ka)):Ka="p_"+h;var Ma=f.rsf[Ka];if(Ma&&Sm(f.rsf,Ka))for(f=0;f<Ma.length;f++){var bb=Ma[f];if(h!==h&&bb.key!==bb.key||h===bb.key)return{id:Ka,
list:Ma,index:f,SNb:bb}}return{id:Ka,list:Ma,index:-1,SNb:void 0}}function bb(h){this.rsf={};this.b4c=f();this.size=0;if(h){h=qb(h);for(var z;!(z=h.next()).done;)z=z.value,this.set(z[0],z[1])}}if(function(){if(!h||"function"!=typeof h||!h.prototype.entries||"function"!=typeof Object.seal)return!1;try{var f=Object.seal({x:4}),z=new h(qb([[f,"s"]]));if("s"!=z.get(f)||1!=z.size||z.get({x:4})||z.set({x:4},"t")!=z||2!=z.size)return!1;var Ka=z.entries(),Ma=Ka.next();if(Ma.done||Ma.value[0]!=f||"s"!=Ma.value[1])return!1;
Ma=Ka.next();return Ma.done||4!=Ma.value[0].x||"t"!=Ma.value[1]||!Ka.next().done?!1:!0}catch(Kb){return!1}}())return h;Ng();var gb=new WeakMap;bb.prototype.set=function(f,h){f=0===f?0:f;var z=Za(this,f);z.list||(z.list=this.rsf[z.id]=[]);z.SNb?z.SNb.value=h:(z.SNb={next:this.b4c,previous:this.b4c.previous,head:this.b4c,key:f,value:h},z.list.push(z.SNb),this.b4c.previous.next=z.SNb,this.b4c.previous=z.SNb,this.size++);return this};bb.prototype.delete=function(f){f=Za(this,f);return f.SNb&&f.list?(f.list.splice(f.index,
1),f.list.length||delete this.rsf[f.id],f.SNb.previous.next=f.SNb.next,f.SNb.next.previous=f.SNb.previous,f.SNb.head=null,this.size--,!0):!1};bb.prototype.clear=function(){this.rsf={};this.b4c=this.b4c.previous=f();this.size=0};bb.prototype.has=function(f){return!!Za(this,f).SNb};bb.prototype.get=function(f){return(f=Za(this,f).SNb)&&f.value};bb.prototype.entries=function(){return Ka(this,function(f){return[f.key,f.value]})};bb.prototype.keys=function(){return Ka(this,function(f){return f.key})};
bb.prototype.values=function(){return Ka(this,function(f){return f.value})};bb.prototype.forEach=function(f,h){for(var z=this.entries(),Ma;!(Ma=z.next()).done;)Ma=Ma.value,f.call(h,Ma[1],Ma[0],this)};bb.prototype[Symbol.iterator]=bb.prototype.entries;var z=0;return bb});function Fw(h,f,Ka){h instanceof String&&(h=String(h));for(var Za=h.length,bb=0;bb<Za;bb++){var gb=h[bb];if(f.call(Ka,gb,bb,h))return{dn:bb,Ju:gb}}return{dn:-1,Ju:void 0}}
Gd("Array.prototype.find",function(h){return h?h:function(f,h){return Fw(this,f,h).Ju}});Gd("String.prototype.startsWith",function(h){return h?h:function(f,h){var Ka=Hd(this,f,"startsWith");f+="";var bb=Ka.length,gb=f.length;h=Math.max(0,Math.min(h|0,Ka.length));for(var z=0;z<gb&&h<bb;)if(Ka[h++]!=f[z++])return!1;return z>=gb}});Gd("Object.is",function(h){return h?h:function(f,h){return f===h?0!==f||1/f===1/h:f!==f&&h!==h}});
Gd("Array.prototype.includes",function(h){return h?h:function(f,h){var Ka=this;Ka instanceof String&&(Ka=String(Ka));var bb=Ka.length;h=h||0;for(0>h&&(h=Math.max(h+bb,0));h<bb;h++){var gb=Ka[h];if(gb===f||Object.is(gb,f))return!0}return!1}});Gd("String.prototype.includes",function(h){return h?h:function(f,h){return-1!==Hd(this,f,"includes").indexOf(f,h||0)}});
Gd("Math.tanh",function(h){return h?h:function(f){f=Number(f);if(0===f)return f;var h=Math.exp(-2*Math.abs(f));h=(1-h)/(1+h);return 0>f?-h:h}});Gd("Math.log1p",function(h){return h?h:function(f){f=Number(f);if(.25>f&&-.25<f){for(var h=f,Za=1,bb=f,gb=0,z=1;gb!=bb;)h*=f,z*=-1,bb=(gb=bb)+z*h/++Za;return bb}return Math.log(1+f)}});Gd("Math.expm1",function(h){return h?h:function(f){f=Number(f);if(.25>f&&-.25<f){for(var h=f,Za=1,bb=f,gb=0;gb!=bb;)h*=f/++Za,bb=(gb=bb)+h;return bb}return Math.exp(f)-1}});
Gd("Math.trunc",function(h){return h?h:function(f){f=Number(f);if(isNaN(f)||Infinity===f||-Infinity===f||0===f)return f;var h=Math.floor(Math.abs(f));return 0>f?-h:h}});Gd("Math.log10",function(h){return h?h:function(f){return Math.log(f)/Math.LN10}});Gd("Math.cosh",function(h){if(h)return h;var f=Math.exp;return function(h){h=Number(h);return(f(h)+f(-h))/2}});Gd("Math.sinh",function(h){if(h)return h;var f=Math.exp;return function(h){h=Number(h);return 0===h?h:(f(h)-f(-h))/2}});
Gd("Math.acosh",function(h){return h?h:function(f){f=Number(f);return Math.log(f+Math.sqrt(f*f-1))}});Gd("Math.atanh",function(h){if(h)return h;var f=Math.log1p;return function(h){h=Number(h);return(f(h)-f(-h))/2}});Gd("Math.asinh",function(h){return h?h:function(f){f=Number(f);if(0===f)return f;var h=Math.log(Math.abs(f)+Math.sqrt(f*f+1));return 0>f?-h:h}});Gd("Array.prototype.findIndex",function(h){return h?h:function(f,h){return Fw(this,f,h).dn}});

Math.imul = Math.imul || function(a, b) {
  var ah = (a >>> 16) & 0xffff;
  var al = a & 0xffff;
  var bh = (b >>> 16) & 0xffff;
  var bl = b & 0xffff;
  // сдвиг на 0 бит закрепляет знак в старшей части числа
  // окончательный |0 преобразует беззнаковое значение обратно в знаковое значение
  return ((al * bl) + (((ah * bl + al * bh) << 16) >>> 0)|0);
};