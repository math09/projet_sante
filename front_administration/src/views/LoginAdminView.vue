<script>
import InputComponent from '../components/InputComponent.vue'
import PrimaryButton from '../components/PrimaryButton.vue'

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
    submitForm() {
      console.log('Email:', this.email);
      console.log('Password:', this.password);
    }
  }
};
</script>

<template>
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 sm:-translate-y-[70%] -translate-y-[50%]">
        <div class="flex justify-center">
          <img src="../assets/logo.png" class="w-100 sm:w-[70%]"/>
        </div>
  
        <div class="flex justify-center gap-5 mt-20 flex-col items-center">
            <InputComponent id="email" label="Adresse mail" v-model-input="email" type="email" class="w-[50%]"/>
            <InputComponent id="password" label="Mot de passe" v-model-input="password" type="password" class="w-[50%]" :value="password"/>
            <PrimaryButton @click="submitForm" class="mt-10">Se connecter</PrimaryButton>
        </div>
    </div>
</template>