<script>
export default {
  methods: {
    goToLogin() {
      this.$router.push({ name: 'login-admin' });
    }
  }
};
</script>

<template>
  <div class="absolute top-1/2 left-1/2 -translate-x-1/2 sm:-translate-y-[70%] -translate-y-[50%]">
    <div class="flex justify-center">
      <img src="../assets/logo.png" class="w-100 sm:w-[70%]"/>
    </div>

    <div class="flex justify-center gap-20 mt-20 sm:flex-row flex-col">
      <button class="flex flex-col justify-center w-52 h-52 text-center shadow-2xl rounded-2xl sm:w-80 sm:h-80 bg-neutral-100" @click="goToLogin">
        <div class="w-full h-full  bg-gradient-to-r from-teal-500 to-teal-300 rounded-t-2xl"></div>
        <h2 class="font-bold text-xl sm:text-2xl p-4">Administration</h2>
      </button>
      <button class="flex flex-col justify-center w-52 h-52 text-center shadow-2xl rounded-2xl sm:w-80 sm:h-80 bg-neutral-100">
        <div class="w-full h-full  bg-gradient-to-r from-green-500 to-green-700 rounded-t-2xl"></div>
        <h2 class="font-bold text-xl sm:text-2xl p-4">Services médicaux</h2>
      </button>
    </div>
  </div>
</template>

<style>

</style>
