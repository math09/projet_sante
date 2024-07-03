<!-- eslint-disable vue/no-mutating-props -->
<script>
import InputComponent from '@/components/InputComponent.vue';
import SearchIcon from '@/components/icons/SearchIcon.vue';
import PrimaryButton from '@/components/PrimaryButton.vue';

export default {
  components: {
    InputComponent,
    SearchIcon,
    PrimaryButton
  },
  props: {
    medicaments: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      medicSelected: []
    }
  },
  methods: {
    selectedMedicament(id) {
      if (this.medicSelected != []) {
        if (this.medicSelected.find(element => element.ref_medicament == id)) {
          this.medicSelected.splice(this.medicaments.indexOf(this.medicaments.find(element => element.ref_medicament == id)), 1)
        }
        else {
          this.medicSelected.push((this.medicaments.find(element => element.ref_medicament == id)))
        }
      }
      else { this.medicSelected.push((this.medicaments.find(element => element.ref_medicament == id))) }
    }
  }
};
</script>

<template>
  <BaseLayout>
    <div class="grid h-full grid-cols-5 gap-3">
      <div class="flex-grow p-2 bg-white rounded-lg">
        <div class="h-full">
          <div class="flex w-full">
            <InputComponent id="search" label="Rechercher" type="text" v-model="search" @input-c="searchInDb"
              input-class="w-full h-4 border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300">
              <SearchIcon />
            </InputComponent>
          </div>
          <br>
          <div class="flex flex-col gap-2 overflow-auto">
            <PrimaryButton v-for="(medicament, index) in medicaments" :key="index"
              @click="selectedMedicament(medicament.ref_medicament)"
              :class="{ 'bg-neutral-200 bg-image-none text-black !shadow-none': medicSelected.find(element => element.ref_medicament == medicament.ref_medicament) == null, 'text-white !shadow-none': medicSelected.find(element => element.ref_medicament == medicament.ref_medicament) != null }"
              >{{ medicament.nom_medicament }} <br> {{ medicament.molecule }}</PrimaryButton>
          </div>
        </div>
      </div>

      <div class="col-span-4 p-2 overflow-hidden bg-white rounded-lg">
        <div class="flex flex-col w-full h-full col-span-3 grid-rows-3 gap-2 p-2 overflow-auto">
          <div class="w-full h-full row-span-1 pb-5">
            <div class="flex justify-between">
              <p class="flex-grow text-lg font-semibold">Médicament sélctionné :</p>
              <PrimaryButton class="text-white px-14" :buttonClass="'!w-fit'">Valider</PrimaryButton>
            </div>
            <div v-for="medic in medicSelected" :key="medic.ref_medicament" class="grid w-full grid-cols-4 gap-2 h-fit">
              <div class="row-span-1">
                - <span>{{ medic.nom_medicament }}</span>
              </div>
              <div class="w-auto row-span-1">
                <p>Date de début : </p> <input class="bg-neutral-200" type="text">
              </div>
              <div class="w-auto row-span-1">
                <p>Date de fin : </p> <input class="bg-neutral-200" type="text">
              </div>
              <div class="w-auto row-span-1">
                <p>Périodicité : </p> <input class="bg-neutral-200" type="text">
              </div>
            </div>
          </div>
          <div class="w-full h-full row-span-2 pb-5">
            <div class="text-lg font-semibold">Champs libre :</div>
            <textarea style="resize: none;" class="w-full h-full rounded-md bg-neutral-200"
              name="diagnostic"></textarea>
          </div>
          <div class="w-full h-full row-span-3 pb-5">
            <div class="text-lg font-semibold">Signature :</div>
            <textarea style="resize: none;" class="w-full h-full rounded-md bg-neutral-200" name="resultat"></textarea>
          </div>
        </div>
      </div>
    </div>
  </BaseLayout>
</template>
