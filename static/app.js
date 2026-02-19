
    const login = document.getElementById('login');
    const app = document.getElementById('app');
    const loginForm = document.getElementById('loginForm');
    const btnMaster = document.getElementById('btn-master');
    const modeModal = document.getElementById('modeModal');
    const modeOk = document.getElementById('modeOk');
    const modeExit = document.getElementById('modeExit');
    const ksuModal = document.getElementById('ksuModal');
    const ksuClose = document.getElementById('ksuClose');
    const newKsuBtn = document.getElementById('newKsuBtn');
    const newKsuModal = document.getElementById('newKsuModal');
    const newKsuClose = document.getElementById('newKsuClose');
    const edit88Btn = document.getElementById('edit88Btn');
    const subfield88Modal = document.getElementById('subfield88Modal');
    const sub88Close = document.getElementById('sub88Close');
    const sub88Ok = document.getElementById('sub88Ok');
    const sub88Cancel = document.getElementById('sub88Cancel');
    const mainTable = document.getElementById('mainTable');
    const distributionTable = document.getElementById('distributionTable');
    const ksuTitle = document.getElementById('ksuTitle');
    const btnDistribution = document.getElementById('btnDistribution');
    const btnMain = document.getElementById('btnMain');
    const ksuInputBtn = document.getElementById('ksuInputBtn');
    const ksuCancel = document.getElementById('ksuCancel');
    const logout = document.getElementById('logout');
    const edit45Btn = document.getElementById('edit45Btn');
    const subfield45Modal = document.getElementById('subfield45Modal');
    const edit47Btn = document.getElementById('edit47Btn');
    const subfield47Modal = document.getElementById('subfield47Modal');
    const edit907Btn = document.getElementById('edit907Btn');
    const subfield907Modal = document.getElementById('subfield907Modal');

    loginForm.addEventListener('submit', e => {
      e.preventDefault();
      login.classList.add('hidden');
      app.classList.remove('hidden');
    });

    btnMaster.addEventListener('click', () => modeModal.classList.remove('hidden'));
    modeExit.addEventListener('click', () => modeModal.classList.add('hidden'));
    modeOk.addEventListener('click', () => {
      modeModal.classList.add('hidden');
      ksuModal.classList.remove('hidden');
    });

    ksuClose.addEventListener('click', () => ksuModal.classList.add('hidden'));

    newKsuBtn.addEventListener('click', () => {
      ksuModal.classList.add('hidden');
      newKsuModal.classList.remove('hidden');
    });
    newKsuClose.addEventListener('click', () => newKsuModal.classList.add('hidden'));

    // Открытие отдельного окна для 88
    edit88Btn.addEventListener('click', () => {
      subfield88Modal.classList.remove('hidden');
    });
    sub88Close.addEventListener('click', () => subfield88Modal.classList.add('hidden'));
    sub88Cancel.addEventListener('click', () => subfield88Modal.classList.add('hidden'));
    sub88Ok.addEventListener('click', () => {
      alert('Подполя 88 сохранены');
      subfield88Modal.classList.add('hidden');
    });

    // Переключение вкладок
    btnDistribution.addEventListener('click', () => {
      mainTable.classList.add('hidden');
      distributionTable.classList.remove('hidden');
      ksuTitle.textContent = 'Данные распределения партии';
      btnMain.classList.remove('bg-indigo-600', 'text-white');
      btnMain.classList.add('bg-gray-200', 'hover:bg-gray-300');
      btnDistribution.classList.add('bg-indigo-600', 'text-white');
      btnDistribution.classList.remove('bg-gray-200', 'hover:bg-gray-300');
    });

    btnMain.addEventListener('click', () => {
      mainTable.classList.remove('hidden');
      distributionTable.classList.add('hidden');
      ksuTitle.textContent = 'Новая запись КСУ';
      btnMain.classList.add('bg-indigo-600', 'text-white');
      btnMain.classList.remove('bg-gray-200', 'hover:bg-gray-300');
      btnDistribution.classList.remove('bg-indigo-600', 'text-white');
      btnDistribution.classList.add('bg-gray-200', 'hover:bg-gray-300');
    });

    ksuInputBtn.addEventListener('click', () => {
      mainTable.classList.remove('hidden');
      distributionTable.classList.add('hidden');
      ksuTitle.textContent = 'Новая запись КСУ';
      btnMain.classList.add('bg-indigo-600', 'text-white');
      btnMain.classList.remove('bg-gray-200', 'hover:bg-gray-300');
      btnDistribution.classList.remove('bg-indigo-600', 'text-white');
      btnDistribution.classList.add('bg-gray-200', 'hover:bg-gray-300');
    });

    ksuCancel.addEventListener('click', () => newKsuModal.classList.add('hidden'));

    // 45, 47, 907 остаются как были
    edit45Btn.addEventListener('click', () => subfield45Modal.classList.remove('hidden'));
    edit47Btn.addEventListener('click', () => subfield47Modal.classList.remove('hidden'));
    edit907Btn.addEventListener('click', () => subfield907Modal.classList.remove('hidden'));

    // Закрытие окон подполей (можно добавить логику сохранения позже)
    document.querySelectorAll('[id$="Close"], [id$="Cancel"]').forEach(btn => {
      btn.addEventListener('click', () => btn.closest('.fixed').classList.add('hidden'));
    });
    document.querySelectorAll('[id$="Ok"]').forEach(btn => {
      btn.addEventListener('click', () => {
        alert('Подполя сохранены');
        btn.closest('.fixed').classList.add('hidden');
      });
    });

    logout.addEventListener('click', () => {
      app.classList.add('hidden');
      login.classList.remove('hidden');
      loginForm.reset();
    });
 