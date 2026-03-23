const fs = require('fs');

const files = [
  'c:/Users/danan/Documents/3Y 1S MODULES/ITPM MODULE/New folder/BrightPath-LMS-ITPM--main/frontend/src/views/Login.vue',
  'c:/Users/danan/Documents/3Y 1S MODULES/ITPM MODULE/New folder/BrightPath-LMS-ITPM--main/frontend/src/views/RegisterView.vue',
  'c:/Users/danan/Documents/3Y 1S MODULES/ITPM MODULE/New folder/BrightPath-LMS-ITPM--main/frontend/src/views/ForgotPassword.vue'
];

files.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  
  content = content.replace(/shadow-\[0_8px_30px_rgb\(0,0,0,0\.04\)\]/g, 'shadow-[0_10px_40px_rgba(0,0,0,0.06)]');
  content = content.replace(/font-extrabold/g, 'font-bold');
  content = content.replace(/tracking-tight/g, '');
  content = content.replace(/font-medium/g, '');
  content = content.replace(/text-\[#0f172a\]/g, 'text-slate-800');
  content = content.replace(/  +/g, ' ');

  fs.writeFileSync(file, content, 'utf8');
});

console.log('Reset complete!');
