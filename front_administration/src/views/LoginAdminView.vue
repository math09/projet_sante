<script>
import InputComponent from '@/components/InputComponent.vue'
import PrimaryButton from '@/components/PrimaryButton.vue'
import axios from '@/utils/axiosInterseptor'

export default {
  name: 'HomePage',
  components: {
    InputComponent,
    PrimaryButton
  },
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post('/login', {
          email: this.email,
          mdp: this.password
        })
        if (response.status == 200) {
          localStorage.setItem("token", response.data.token)
          this.$router.push({ name: "home" });
        }
      } catch (error) {
        if (error.response) {
          console.error("Erreur de requête:", error.response.data);
        } else if (error.request) {
          console.error("Aucune réponse reçue:", error.request);
        } else {
          console.error("Erreur de configuration de la requête:", error.message);
        }
      }
    }
  }
};
</script>

<template>
  <div class="absolute top-1/2 left-1/2 -translate-x-1/2 sm:-translate-y-[70%] -translate-y-[50%]">
    <div class="flex justify-center">
      <img src="@/assets/logo.png" class="w-100 sm:w-[70%]" />
    </div>

    <div class="flex justify-center gap-5 mt-20 flex-col items-center">
      <InputComponent id="email" label="Adresse mail" v-model="email" type="email" class="w-[50%]" />
      <InputComponent id="password" label="Mot de passe" v-model="password" type="password" class="w-[50%]" />
      <PrimaryButton @click="submitForm" class="mt-10">Se connecter</PrimaryButton>
    </div>
  </div>
</template>