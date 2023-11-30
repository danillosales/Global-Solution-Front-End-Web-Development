function scrollScreen(sectionId) {
    sectionId = (sectionId.includes('#') ? '' : '#') + sectionId;
  
    const section = document.querySelector(sectionId);
    console.log(section);
    if (section) {
      const navHeight = document.querySelector('nav').clientHeight;
  
      document.querySelector('main').scrollTo({
        top: section.offsetTop - navHeight,
        behavior: 'smooth'
      });
    }
  }
  

function sendMe() {
    let error = false;
  
    const email = document.querySelector('#email');
    const name = document.querySelector('#name')
    if (!email.checkValidity()) {
      email.classList.add('invalid');
      error = true;
    }
    else {
      email.classList.remove('invalid');
    }
  
    if (!error) {
      alert('Você será avisado!');
      email.value = '';
      name.value = '';
    }
}