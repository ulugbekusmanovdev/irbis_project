document.addEventListener("DOMContentLoaded", () => {

      const login = document.getElementById('login');
      const app = document.getElementById('app');
      const loginForm = document.getElementById('loginForm');

      const btnKomplektator = document.getElementById('btn-komplektator');
      const ksuPage = document.getElementById('ksuPage');
      const homeContent = document.getElementById('homeContent');

      const newKsuBtn = document.getElementById('newKsuBtn');
      const blockDefault = document.getElementById('blockDefault');
      const blockKsu = document.getElementById('blockKsu');

      const submitBtn = document.getElementById('ksuInputBtn');
      const cancelBtn = document.getElementById('ksuCancel');

      const logout = document.getElementById('logout');

      // --- модалки ---
      const edit88Btn = document.getElementById('edit88Btn');
      const subfield88Modal = document.getElementById('subfield88Modal');

      const edit907Btn = document.getElementById('edit907Btn');
      const subfield907Modal = document.getElementById('subfield907Modal');

      const edit45Btn = document.getElementById('edit45Btn');
      const subfield45Modal = document.getElementById('subfield45Modal');

      const edit47Btn = document.getElementById('edit47Btn');
      const subfield47Modal = document.getElementById('subfield47Modal');
      const btnMain = document.getElementById('btnMain');
      const btnDistribution = document.getElementById('btnDistribution');

      const mainTable = document.getElementById('mainTable');
      const distributionTable = document.getElementById('distributionTable');

      if (btnDistribution) {
        btnDistribution.addEventListener('click', () => {
          mainTable.classList.add('hidden');
          distributionTable.classList.remove('hidden');

          btnDistribution.classList.add('bg-indigo-600', 'text-white');
          btnDistribution.classList.remove('bg-gray-200');

          btnMain.classList.remove('bg-indigo-600', 'text-white');
          btnMain.classList.add('bg-gray-200');
        });
      }

      if (btnMain) {
        btnMain.addEventListener('click', () => {
          mainTable.classList.remove('hidden');
          distributionTable.classList.add('hidden');

          btnMain.classList.add('bg-indigo-600', 'text-white');
          btnMain.classList.remove('bg-gray-200');

          btnDistribution.classList.remove('bg-indigo-600', 'text-white');
          btnDistribution.classList.add('bg-gray-200');
        });
      }

      // --- LOGIN ---
      if (loginForm) {
        loginForm.addEventListener('submit', e => {
          e.preventDefault();
          login.classList.add('hidden');
          app.classList.remove('hidden');
        });
      }

      // --- НАВИГАЦИЯ ---
      if (btnKomplektator) {
        btnKomplektator.addEventListener('click', () => {
          homeContent.classList.add('hidden');
          ksuPage.classList.remove('hidden');
        });
      }

      // --- КСУ ---
      if (newKsuBtn) {
        newKsuBtn.addEventListener("click", () => {
          blockDefault.classList.add("hidden");
          blockKsu.classList.remove("hidden");
        });
      }

      if (cancelBtn) {
        cancelBtn.addEventListener("click", () => {
          blockKsu.classList.add("hidden");
          blockDefault.classList.remove("hidden");
        });
      }

      if (submitBtn) {
        submitBtn.addEventListener("click", () => {
          const val88 = document.querySelector("#field88Value")?.value.trim();
          const val907 = document.querySelector("#field907Value")?.value.trim();

          if (!val88) return alert("Заполните поле 88");

          alert(`Сохранено:\n88: ${val88}\n907: ${val907}`);

          blockKsu.classList.add("hidden");
          blockDefault.classList.remove("hidden");
        });
      }

      // --- МОДАЛКИ ---
      if (edit88Btn) {
        edit88Btn.addEventListener('click', () => {
          subfield88Modal.classList.remove('hidden');
        });
      }

      if (edit907Btn) {
        edit907Btn.addEventListener('click', () => {
          subfield907Modal.classList.remove('hidden');
        });
      }

      if (edit45Btn) {
        edit45Btn.addEventListener('click', () => {
          subfield45Modal.classList.remove('hidden');
        });
      }

      if (edit47Btn) {
        edit47Btn.addEventListener('click', () => {
          subfield47Modal.classList.remove('hidden');
        });
      }

      // --- ЗАКРЫТИЕ МОДАЛОК ---
      document.querySelectorAll('[id$="Close"], [id$="Cancel"]').forEach(btn => {
        btn.addEventListener('click', () => {
          btn.closest('.fixed')?.classList.add('hidden');
        });
      });

      document.querySelectorAll('[id$="Ok"]').forEach(btn => {
        btn.addEventListener('click', () => {
          alert('Подполя сохранены');
          btn.closest('.fixed')?.classList.add('hidden');
        });
      });

      // --- LOGOUT ---
      if (logout) {
        logout.addEventListener('click', () => {
          app.classList.add('hidden');
          login.classList.remove('hidden');
          loginForm.reset();
        });
      }

    });