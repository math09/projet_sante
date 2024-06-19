<template>
    <div class="flex flex-col">
      <label v-if="label" :for="id" class="mb-2 font-semibold text-md" :class="labelClass">{{ label }}</label>
      <input
        :id="id"
        :type="type"
        :value="value"
        :placeholder="placeholder"
        :disabled="disabled"
        v-model="test"
        class="p-5 text-xl border border-gray-50 focus:outline-none focus:border-gray-200 bg-neutral-100 shadow-xl rounded-2xl"
        :class="inputClass"
      />
    </div>
</template>

<script setup>
import { defineModel } from 'vue';

const test = defineModel('modelValue');
</script>

<script>
  export default {
    name: 'InputComponent',
    props: {
      id: {
        type: String,
        default: ''
      },
      type: {
        type: String,
        default: 'text'
      },
      value: {
        type: String,
        default: ''
      },
      placeholder: {
        type: String,
        default: ''
      },
      disabled: {
        type: Boolean,
        default: false
      },
      label: {
        type: String,
        default: ''
      },
      inputClass: {
        type: String,
        default: ''
      },
      labelClass: {
        type: String,
        default: ''
      }
    }
  };
</script>