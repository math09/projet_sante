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
    examens: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      examSelected: null,
      motif: "",
      diagnostic: "",
      analyse: "",
      conclusion: "",
      observation: "",
      search: ""
    }
  },
  methods: {
    selectedExamen(id) {
      if (id == this.examSelected) this.examSelected = null;
      else this.examSelected = id;
    },
    submitExam(){
      this.$emit('submit_exam', {
        motif: this.motif,
        diagnostic: this.diagnostic,
        analyse: this.analyse,
        conclusion: this.conclusion,
        observation: this.observation
      });
      setTimeout(() => {
        this.examSelected = null;
        this.motif = "";
        this.diagnostic = "";
        this.analyse = "";
        this.conclusion = "";
        this.observation = "";
      }, 100);
    }
  },
  watch: {
    examens() {
      this.examSelected = null;
    }
  },
  computed: {
    filteredExamen() {
      const searchTerm = this.search.toLowerCase();
      return this.examens.filter(exam =>
        exam.motif.toLowerCase().includes(searchTerm)
      );
    }
  }
};
</script>

<template>
  <BaseLayout>
    <div class="grid h-full grid-cols-5 gap-2">
      <div class="p-2 bg-white rounded-lg">
        <div class="h-full">
          <div class="w-full">
            <InputComponent id="search" label="Rechercher" type="text" v-model="search"
              input-class="w-full h-4 border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300">
              <SearchIcon />
            </InputComponent>
          </div>
          <div class="flex flex-col gap-2 overflow-auto mt-5">
            <PrimaryButton v-for="(examen, index) in filteredExamen" :key="index" @click="selectedExamen(examen.id_examens)"
              class='mb-2 !shadow-none' :buttonClass="{'bg-neutral-200 bg-image-none text-black':examen.id_examens!=examSelected, 'text-white':examen.id_examens==examSelected}">{{ examen.date }} <br> {{ examen.motif }}</PrimaryButton>
          </div>
        </div>
      </div>

      <div class="col-span-4 p-2 overflow-hidden bg-white rounded-lg">
        <div class="flex flex-col h-full col-span-3 gap-6 p-2">
          <div v-if="this.examSelected != null" class="grid w-full h-full grid-cols-3 gap-2">
            <div class="w-full h-full col-span-2 row-span-1 pb-5">
              <h5 class="font-semibold text-lg">Motif :</h5>
              <p class="w-full h-full bg-mercury-200 rounded-lg py-1.5 px-2">{{ examens.find(examen => examen.id_examens == examSelected).motif }}
              </p>
            </div>
            <div class="w-full h-full col-span-1 row-span-3 pb-5">
              <h5 class="font-semibold text-lg">Diagnostic :</h5>
              <p class="w-full h-full bg-mercury-200 rounded-lg py-1.5 px-2">{{ examens.find(examen =>
              examen.id_examens == examSelected).diagnostic }}</p>
            </div>
            <div class="w-full h-full col-span-2 row-span-2 pb-5">
              <h5 class="font-semibold text-lg">Résultats d'analyse :</h5>
              <p class="w-full h-full bg-mercury-200 rounded-lg py-1.5 px-2">{{ examens.find(examen =>
              examen.id_examens == examSelected).resultat_analyse }}</p>
            </div>
            <div class="w-full h-full col-span-2 row-span-2 pb-5">
              <h5 class="w-full h-fit font-semibold text-lg">Conclusion :</h5>
              <p class="w-full h-full bg-mercury-200 rounded-lg py-1.5 px-2">{{ examens.find(examen =>
              examen.id_examens == examSelected).conclusion }}</p>
            </div>
            <div class="w-full h-full col-span-1 row-span-2 pb-5">
              <h5 class="font-semibold text-lg">Observation :</h5>
              <p class="w-full h-full bg-mercury-200 rounded-lg py-1.5 px-2">{{ examens.find(examen =>
                examen.id_examens==examSelected).observation }}</p>
            </div>
          </div>

          <div class="flex flex-col h-full pb-2" v-else>
            <div class="flex justify-end">
              <PrimaryButton class="text-white !w-fit px-14" @click="submitExam">Valider</PrimaryButton>
            </div>
            <div class="grid w-full h-full grid-cols-3 gap-2 flex-grow">
              <div class="w-full h-full col-span-2 row-span-1 pb-5">
                <h5 class="w-full h-fit font-semibold text-lg">Motif :</h5>
                <textarea v-model="motif" style="resize: none;" class="w-full h-full bg-mercury-200 rounded-lg px-2 py-1.5" name="motif"></textarea>
              </div>
              <div class="w-full h-full col-span-1 row-span-3 pb-5">
                <h5 class="w-full h-fit font-semibold text-lg">Diagnostic :</h5>
                <textarea v-model="diagnostic" style="resize: none;" class="w-full h-full bg-mercury-200 rounded-lg px-2 py-1.5" name="diagnostic"></textarea>
              </div>
              <div class="w-full h-full col-span-2 row-span-2 pb-5">
                <h5 class="w-full h-fit font-semibold text-lg">Résultats d'analyse :</h5>
                <textarea v-model="analyse" style="resize: none;" class="w-full h-full bg-mercury-200 rounded-lg px-2 py-1.5" name="resultat"></textarea>
              </div>
              <div class="w-full h-full col-span-2 row-span-2 pb-5">
                <h5 class="w-full h-fit font-semibold text-lg">Conclusion :</h5>
                <textarea v-model="conclusion" style="resize: none;" class="w-full h-full bg-mercury-200 rounded-lg px-2 py-1.5" name="conclusion"></textarea>
              </div>
              <div class="w-full h-full col-span-1 row-span-2 pb-5">
                <h5 class="relative font-semibold text-lg">Observation :</h5>
                <textarea v-model="observation" style="resize: none;" class="w-full h-full bg-mercury-200 rounded-lg px-2 py-1.5" name="observation"></textarea>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>


  </BaseLayout>
</template>
