<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import api from '../api/axios'
import AppNavbar from '../components/layout/AppNavbar.vue'

const router = useRouter()

const universityData = {
  "University of Moratuwa": {
    "Engineering": ["Computer Science & Engineering", "Civil Engineering", "Mechanical Engineering", "Electrical Engineering"],
    "IT": ["Information Technology", "Artificial Intelligence"],
    "Architecture": ["Architecture", "Town & Country Planning"],
    "Business": ["Business Science", "Financial Analytics"]
  },
  "University of Colombo": {
    "UCSC": ["Computer Science", "Software Engineering", "Information Systems"],
    "Science": ["Biological Science", "Physical Science"],
    "Arts": ["Economics", "Geography", "History"],
    "Management": ["Accounting", "Finance", "Human Resources"],
    "Medicine": ["Medicine", "Physiotherapy"],
    "Education": ["Education"]
  },
  "University of Peradeniya": {
    "Engineering": ["Civil Engineering", "Computer Engineering"],
    "Science": ["Biological Science", "Physical Science"],
    "Arts": ["Fine Arts", "Sociology"],
    "Agriculture": ["Agricultural Technology"],
    "Medicine": ["Medicine"],
    "Dental": ["Dental Surgery"],
    "Vet Science": ["Veterinary Medicine"]
  },
  "University of Sri Jayewardenepura": {
    "Applied Sciences": ["Computer Science", "Physics"],
    "Management": ["Business Administration"],
    "Humanities": ["English", "History"],
    "Engineering": ["Civil Engineering"],
    "Technology": ["Information Communication Technology"],
    "Medicine": ["Medicine"]
  },
  "University of Kelaniya": {
    "Computing & Tech": ["Software Engineering", "Computer Science"],
    "Science": ["Physics", "Mathematics"],
    "Commerce & Management": ["Commerce", "Business Management"],
    "Humanities": ["Linguistics", "Buddhist Studies"],
    "Medicine": ["Medicine"]
  },
  "University of Ruhuna": {
    "Science": ["Computer Science", "Mathematics"],
    "Management": ["Business Administration"],
    "Arts": ["Geography"]
  },
  "University of Jaffna": {
    "Science": ["Computer Science", "Physics"],
    "Management": ["Business Administration"],
    "Arts": ["History"]
  },
  "Eastern University": {
    "Science": ["Biology", "Chemistry"],
    "Management": ["Business Administration"],
    "Arts": ["Sociology"]
  },
  "Rajarata University": {
    "Science": ["Applied Sciences"],
    "Management": ["Business Management"],
    "Arts": ["Social Sciences"]
  },
  "Wayamba University": {
    "Science": ["Applied Sciences"],
    "Management": ["Business Management"],
    "Arts": ["General Arts"]
  },
  "Sabaragamuwa University": {
    "Science": ["Computing", "Physical Education"],
    "Management": ["Business Management"],
    "Arts": ["Languages"]
  },
  "South Eastern University": {
    "Science": ["Applied Sciences"],
    "Management": ["Islamic Studies", "Business Administration"],
    "Arts": ["Arts & Culture"]
  },
  "Uva Wellassa University": {
    "Science": ["Computer Science", "Industrial IT"],
    "Management": ["Entrepreneurship"],
    "Arts": ["Tourism"]
  },
  "SLIIT": {
    "Computing": ["Information Technology", "Software Engineering", "Computer Systems & Network Engineering", "Information Systems Engineering", "Interactive Media", "Cyber Security", "Data Science"],
    "Business": ["Business Management"],
    "Engineering": ["Civil Engineering"],
    "Humanities & Sciences": ["Biotechnology", "Nursing"]
  },
  "NSBM": {
    "Computing": ["Computer Science", "Software Engineering"],
    "Business": ["Business Management", "Accounting"],
    "Engineering": ["Mechatronics"]
  },
  "IIT": {
    "Computing": ["Software Engineering", "Computer Science"],
    "Business": ["Business Information Systems"]
  },
  "Horizon Campus": {
    "Computing": ["Information Technology", "Computer Science"],
    "Business": ["Business Management"]
  },
  "CINEC": {
    "Computing": ["Software Engineering", "IT"],
    "Engineering": ["Marine Engineering", "Mechanical Engineering"]
  },
  "SLTC": {
    "Computing": ["Software Engineering", "IT"],
    "Engineering": ["Electronics", "Telecommunication"]
  }
}

const currentStep = ref(1)
const selectedRole = ref(null)

const roles = [
  { id: 'STUDENT', title: 'STUDENT', icon: 'M12 14l9-5-9-5-9 5 9 5z' },
  { id: 'LECTURER', title: 'LECTURER', icon: 'M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10' },
  { id: 'STAFF', title: 'STAFF', icon: 'M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z' }
]

const formData = ref({
  fullName: '',
  email: '',
  password: '',
  nicNumber: '',
  phoneNumber: '',

  // Student
  studentId: '',
  university: '',
  faculty: '',
  academicStream: '',
  academicYear: '',
  idPhoto: null,
  idPhotoPreview: null,
  isPeerTutor: false,

  // Lecturer
  lecturerInstitution: '',
  lecturerDepartment: '',
  lecturerDesignation: '',
  lecturerVerificationDoc: null,
  lecturerDocPreview: null,
  
  // Staff
  staffDepartment: '',
  staffId: ''
})

const universitySearchQuery = ref('')
const isUniversityDropdownOpen = ref(false)

const errors = ref({})
const isLoading = ref(false)
const showPassword = ref(false)
const fileInputRef = ref(null)
const docInputRef = ref(null)

const availableUniversities = computed(() => Object.keys(universityData))

const filteredUniversities = computed(() => {
  if (!universitySearchQuery.value) return availableUniversities.value
  const query = universitySearchQuery.value.toLowerCase()
  return availableUniversities.value.filter(uni => uni.toLowerCase().includes(query))
})

const onUniversityInput = () => {
  formData.value.university = '' 
  formData.value.faculty = ''
  formData.value.academicStream = ''
  isUniversityDropdownOpen.value = true
}

const selectUniversity = (uni) => {
  formData.value.university = uni
  universitySearchQuery.value = uni
  isUniversityDropdownOpen.value = false
  onUniversityChange()
}

const availableFaculties = computed(() => {
  if (!formData.value.university) return []
  return Object.keys(universityData[formData.value.university] || {})
})

const availableStreams = computed(() => {
  if (!formData.value.university || !formData.value.faculty) return []
  return universityData[formData.value.university][formData.value.faculty] || []
})

const onUniversityChange = () => {
  formData.value.faculty = ''
  formData.value.academicStream = ''
}

const onFacultyChange = () => {
  formData.value.academicStream = ''
}

const triggerFileInput = () => {
  if (fileInputRef.value) fileInputRef.value.click()
}
const onFileChange = (e) => {
  const file = e.target.files[0]
  if (file) processFile(file)
}
const processFile = (file) => {
  if (file.type === 'image/jpeg' || file.type === 'image/png') {
    if (file.size <= 2 * 1024 * 1024) {
      formData.value.idPhoto = file
      formData.value.idPhotoPreview = URL.createObjectURL(file)
      errors.value.idPhoto = ''
    } else {
      errors.value.idPhoto = 'File size exceeds 2MB limit.'
      removePhoto()
    }
  } else {
    errors.value.idPhoto = 'Please upload a valid JPG or PNG image.'
    removePhoto()
  }
}
const removePhoto = () => {
  if (formData.value.idPhotoPreview && formData.value.idPhotoPreview.startsWith('blob:')) {
    URL.revokeObjectURL(formData.value.idPhotoPreview)
  }
  formData.value.idPhoto = null
  formData.value.idPhotoPreview = null
  if (fileInputRef.value) fileInputRef.value.value = ''
}

const triggerDocInput = () => {
  if (docInputRef.value) docInputRef.value.click()
}
const onDocChange = (e) => {
  const file = e.target.files[0]
  if (file) {
    if (file.size <= 5 * 1024 * 1024) {
      formData.value.lecturerVerificationDoc = file
      formData.value.lecturerDocPreview = file.name
      errors.value.lecturerVerificationDoc = ''
    } else {
      errors.value.lecturerVerificationDoc = 'File size exceeds 5MB limit.'
      removeDoc()
    }
  }
}
const removeDoc = () => {
  formData.value.lecturerVerificationDoc = null
  formData.value.lecturerDocPreview = null
  if (docInputRef.value) docInputRef.value.value = ''
}

const fillDemoData = () => {
  const svgTemplate = encodeURIComponent(`<svg xmlns="http://www.w3.org/2000/svg" width="400" height="250" style="background:#f8fafc; border-radius:12px; font-family:-apple-system,system-ui,sans-serif; border: 1px solid #e2e8f0"><rect width="100%" height="100%" fill="#f8fafc"/><text x="50%" y="40%" font-size="24" fill="#6B7280" font-weight="700" text-anchor="middle" dominant-baseline="middle">Student ID Card</text><rect x="40" y="30" width="70" height="90" rx="6" fill="#cbd5e1"/><rect x="130" y="45" width="160" height="12" rx="4" fill="#94a3b8"/><rect x="130" y="75" width="100" height="8" rx="4" fill="#cbd5e1"/><rect x="130" y="95" width="130" height="8" rx="4" fill="#cbd5e1"/></svg>`)
  const mockupUrl = `data:image/svg+xml;charset=utf-8,${svgTemplate}`

  formData.value.fullName = 'Jane Doe'
  formData.value.email = 'jane.doe@example.com'
  formData.value.password = 'SecurePassword123!'
  formData.value.nicNumber = '991234567V'
  formData.value.phoneNumber = '0771234567'

  if (selectedRole.value === 'STUDENT') {
    formData.value.studentId = 'IT21005678'
    formData.value.university = 'University of Moratuwa'
    formData.value.faculty = 'Engineering'
    formData.value.academicStream = 'Computer Science & Engineering'
    formData.value.academicYear = 'Year 2'
    formData.value.idPhoto = new File(["dummy"], "student_id.jpg", { type: "image/jpeg" })
    formData.value.idPhotoPreview = mockupUrl
    formData.value.isPeerTutor = true
    universitySearchQuery.value = 'University of Moratuwa'
  } else if (selectedRole.value === 'LECTURER') {
    formData.value.lecturerInstitution = 'SLIIT'
    formData.value.lecturerDepartment = 'Software Engineering'
    formData.value.lecturerDesignation = 'Senior Lecturer'
    formData.value.lecturerVerificationDoc = new File(["dummy"], "verification.pdf", { type: "application/pdf" })
    formData.value.lecturerDocPreview = 'verification.pdf'
  } else if (selectedRole.value === 'STAFF') {
    formData.value.staffDepartment = 'Administration'
    formData.value.staffId = 'STF9938'
  }
  errors.value = {}
}

const validateForm = () => {
  const newErrors = {}
  
  const nicRegex = /^([0-9]{9}[vVxX]|[0-9]{12})$/
  const phoneRegex = /^[0-9]{10}$/
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

  if (!formData.value.fullName) {
    newErrors.fullName = 'Full Name is required.'
  } else if (!/^[a-zA-Z\s]+$/.test(formData.value.fullName)) {
    newErrors.fullName = 'Full Name should only contain letters and spaces.'
  }

  if (!formData.value.email) {
    newErrors.email = 'Email Address is required.'
  } else if (!emailRegex.test(formData.value.email)) {
    newErrors.email = 'Please enter a valid email address.'
  }

  if (!formData.value.password) {
    newErrors.password = 'Password is required.'
  } else if (formData.value.password.length < 8) {
    newErrors.password = 'Password must be at least 8 characters.'
  }

  if (!formData.value.nicNumber) {
    newErrors.nicNumber = 'NIC Number is required.'
  } else if (!nicRegex.test(formData.value.nicNumber)) {
    newErrors.nicNumber = 'Invalid NIC format (9 digits + V/X or 12 digits).'
  }

  if (formData.value.phoneNumber && !phoneRegex.test(formData.value.phoneNumber)) {
    newErrors.phoneNumber = 'Phone number must be exactly 10 digits.'
  }

  if (selectedRole.value === 'STUDENT') {
    if (!formData.value.university) newErrors.university = 'University is required.'
    if (!formData.value.studentId) newErrors.studentId = 'Student ID is required.'
    if (!formData.value.faculty) newErrors.faculty = 'Faculty is required.'
    if (!formData.value.academicStream) newErrors.academicStream = 'Academic Stream is required.'
    if (!formData.value.academicYear) newErrors.academicYear = 'Academic Year is required.'
  } else if (selectedRole.value === 'LECTURER') {
    if (!formData.value.lecturerInstitution) newErrors.lecturerInstitution = 'Institution is required.'
    if (!formData.value.lecturerDepartment) newErrors.lecturerDepartment = 'Department is required.'
    if (!formData.value.lecturerDesignation) newErrors.lecturerDesignation = 'Designation is required.'
  } else if (selectedRole.value === 'STAFF') {
    if (!formData.value.staffDepartment) newErrors.staffDepartment = 'Department is required.'
    if (!formData.value.staffId) newErrors.staffId = 'Staff ID is required.'
  }

  errors.value = newErrors
  return Object.keys(newErrors).length === 0
}

const handleRegister = async () => {
  if (!validateForm()) return
  isLoading.value = true
  errors.value = {}

  console.log('DEBUG: Registration process started')
  console.log('DEBUG: Selected Role:', selectedRole.value)

  try {
    const formDataPayload = new FormData()
    
    // Core fields
    formDataPayload.append('username', formData.value.email)
    formDataPayload.append('email', formData.value.email)
    formDataPayload.append('password', formData.value.password)
    formDataPayload.append('role', selectedRole.value)
    formDataPayload.append('full_name', formData.value.fullName)
    formDataPayload.append('nic_number', formData.value.nicNumber)
    formDataPayload.append('phone_number', formData.value.phoneNumber)

    // Role-specific fields
    if (selectedRole.value === 'STUDENT') {
      formDataPayload.append('university', formData.value.university)
      formDataPayload.append('faculty', formData.value.faculty)
      formDataPayload.append('academic_stream', formData.value.academicStream)
      formDataPayload.append('student_id', formData.value.studentId)
      formDataPayload.append('is_peer_tutor', formData.value.isPeerTutor)
      if (formData.value.idPhoto) {
        formDataPayload.append('id_photo', formData.value.idPhoto)
      }
    } else if (selectedRole.value === 'LECTURER') {
      formDataPayload.append('institution', formData.value.lecturerInstitution)
      formDataPayload.append('department', formData.value.lecturerDepartment)
      formDataPayload.append('designation', formData.value.lecturerDesignation)
      if (formData.value.lecturerVerificationDoc) {
        formDataPayload.append('verification_doc', formData.value.lecturerVerificationDoc)
      }
    } else if (selectedRole.value === 'STAFF') {
      formDataPayload.append('department', formData.value.staffDepartment)
      formDataPayload.append('student_id', formData.value.staffId) // Staff ID stored in student_id field
    }

    console.log('DEBUG: FormData prepared. Sending request...')
    
    // Exact endpoint as requested: http://127.0.0.1:8000/api/accounts/register/
    const response = await api.post('http://127.0.0.1:8000/api/accounts/register/', formDataPayload, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    
    console.log('DEBUG: API Response Status:', response.status)
    console.log('DEBUG: API Response Data:', response.data)

    if (response.status === 201) {
      alert('Registration Successful!')
      router.push('/login')
    }
  } catch (err) {
    console.error('DEBUG: Registration Error:', err)
    if (err.response && err.response.data) {
      console.log('DEBUG: API Error Data:', err.response.data)
      const apiErrors = err.response.data
      const newErrors = {}
      
      Object.keys(apiErrors).forEach(key => {
        const camelKey = key.replace(/_([a-z])/g, (g) => g[1].toUpperCase())
        newErrors[camelKey] = Array.isArray(apiErrors[key]) ? apiErrors[key][0] : apiErrors[key]
      })
      
      errors.value = newErrors
    } else {
      alert('An unexpected error occurred. Please try again.')
    }
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen bg-hero-bg-pill flex flex-col font-sans text-content relative overflow-hidden">
    <div class="absolute top-0 right-0 w-1/3 h-full bg-hero-bg-right clip-path-slant z-0 opacity-20"></div>

    <AppNavbar class="z-20 relative" />
    
    <main class="flex-1 flex items-center justify-center p-4 sm:p-8 z-10 relative">
      <div class="w-full max-w-4xl bg-white rounded-[2rem] shadow-[0_10px_40px_rgba(0,0,0,0.06)] border border-slate-100 overflow-hidden relative" :style="currentStep === 2 ? 'max-height: calc(100vh - 120px); overflow-y: auto;' : ''">
        
        <!-- Step 1: Role Selection Screen -->
        <div v-if="currentStep === 1" class="p-8 sm:p-14 relative z-10 text-center animate-fade-in-up flex flex-col items-center justify-center w-full">
          <h1 class="text-4xl font-bold text-slate-800 mb-3">Create an Account</h1>
          <p class="text-slate-500 mb-12 text-lg">Welcome to the BrightPath Learning Community! Please select your role to get started.</p>

          <div class="flex flex-col sm:flex-row justify-center gap-6 sm:gap-8 w-full max-w-5xl">
            <!-- STUDENT CARD -->
            <div @click="selectedRole = 'STUDENT'"
              class="bg-white border-2 rounded-3xl w-full sm:w-52 sm:h-52 p-6 flex flex-col items-center justify-center cursor-pointer transition-all duration-300 relative overflow-hidden group aspect-square"
              :class="selectedRole === 'STUDENT' ? 'border-[3px] border-hero-highlight bg-[#97C4C4]/5 shadow-[0_10px_30px_rgba(107,70,193,0.15)] transform -translate-y-2' : 'border-slate-100 shadow-sm hover:border-hero-highlight/40 hover:shadow-[0_10px_25px_rgba(107,70,193,0.08)] hover:-translate-y-1.5'">
              <div class="absolute inset-0 bg-gradient-to-b from-transparent to-[#97C4C4]/10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
              <div class="w-20 h-20 rounded-full flex items-center justify-center mb-4 transition-all duration-300 relative z-10"
                :class="selectedRole === 'STUDENT' ? 'text-hero-highlight scale-110 bg-hero-highlight/10' : 'text-slate-800 group-hover:text-hero-highlight bg-slate-50'">
                <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 10v6M2 10l10-5 10 5-10 5z"></path>
                  <path d="M6 12v5c3 3 9 3 12 0v-5"></path>
                </svg>
              </div>
              <h3 class="font-bold text-2xl text-slate-800 tracking-widest relative z-10 mt-2">STUDENT</h3>
            </div>

            <!-- LECTURER CARD -->
            <div @click="selectedRole = 'LECTURER'"
              class="bg-white border-2 rounded-3xl w-full sm:w-52 sm:h-52 p-6 flex flex-col items-center justify-center cursor-pointer transition-all duration-300 relative overflow-hidden group aspect-square"
              :class="selectedRole === 'LECTURER' ? 'border-[3px] border-hero-highlight bg-[#97C4C4]/5 shadow-[0_10px_30px_rgba(107,70,193,0.15)] transform -translate-y-2' : 'border-slate-100 shadow-sm hover:border-hero-highlight/40 hover:shadow-[0_10px_25px_rgba(107,70,193,0.08)] hover:-translate-y-1.5'">
              <div class="absolute inset-0 bg-gradient-to-b from-transparent to-[#97C4C4]/10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
              <div class="w-20 h-20 rounded-full flex items-center justify-center mb-4 transition-all duration-300 relative z-10"
                :class="selectedRole === 'LECTURER' ? 'text-hero-highlight scale-110 bg-hero-highlight/10' : 'text-slate-800 group-hover:text-hero-highlight bg-slate-50'">
                <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M2 3h20M21 3v11a2 2 0 01-2 2H5a2 2 0 01-2-2V3m7 19v-4m4 4v-4m-4 0h4"></path>
                </svg>
              </div>
              <h3 class="font-bold text-2xl text-slate-800 tracking-widest relative z-10 mt-2">LECTURER</h3>
            </div>

            <!-- STAFF CARD -->
            <div @click="selectedRole = 'STAFF'"
              class="bg-white border-2 rounded-3xl w-full sm:w-52 sm:h-52 p-6 flex flex-col items-center justify-center cursor-pointer transition-all duration-300 relative overflow-hidden group aspect-square"
              :class="selectedRole === 'STAFF' ? 'border-[3px] border-hero-highlight bg-[#97C4C4]/5 shadow-[0_10px_30px_rgba(107,70,193,0.15)] transform -translate-y-2' : 'border-slate-100 shadow-sm hover:border-hero-highlight/40 hover:shadow-[0_10px_25px_rgba(107,70,193,0.08)] hover:-translate-y-1.5'">
              <div class="absolute inset-0 bg-gradient-to-b from-transparent to-[#97C4C4]/10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
              <div class="w-20 h-20 rounded-full flex items-center justify-center mb-4 transition-all duration-300 relative z-10"
                :class="selectedRole === 'STAFF' ? 'text-hero-highlight scale-110 bg-hero-highlight/10' : 'text-slate-800 group-hover:text-hero-highlight bg-slate-50'">
                <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2z"></path>
                  <circle cx="9" cy="12" r="2"></circle>
                  <path d="M14 11h4M14 14h2"></path>
                </svg>
              </div>
              <h3 class="font-bold text-2xl text-slate-800 tracking-widest relative z-10 mt-2">STAFF</h3>
            </div>
          </div>

          <div class="mt-[50px] flex justify-center w-full">
            <button @click="currentStep = 2" :disabled="!selectedRole"
              class="w-full sm:w-auto min-w-[300px] bg-hero-highlight hover:bg-hero-highlight/90 text-white font-bold py-4 px-12 rounded-full transition-all duration-300 shadow-[0_10px_30px_rgba(107,70,193,0.25)] disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none transform hover:-translate-y-1 hover:scale-105 tracking-widest text-[1.1rem] uppercase">
              {{ selectedRole ? 'JOIN AS ' + selectedRole : 'SELECT A ROLE' }}
            </button>
          </div>
          
          <p class="text-center mt-12 pb-8 text-sm text-slate-500 ">
            Already have an account? 
            <router-link to="/login" class="text-hero-highlight hover:opacity-80 font-bold transition-opacity">LOGIN</router-link>
          </p>
        </div>

        <!-- Step 2: Role-Specific Form -->
        <div v-if="currentStep === 2" class="p-8 sm:p-12 relative z-10 animate-fade-in-up">
          <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-10 relative">
            <button type="button" @click="currentStep = 1" 
              class="text-sm font-bold text-slate-400 hover:text-hero-highlight transition-colors flex items-center gap-2 mb-6 sm:mb-0 border border-slate-200 px-4 py-2 rounded-full hover:bg-slate-50 relative top-1">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"></path></svg>
              BACK TO ROLES
            </button>
            <h1 class="text-2xl sm:text-3xl font-bold text-content sm:absolute sm:left-1/2 sm:-translate-x-1/2 uppercase">{{ selectedRole }} REGISTRATION</h1>
            <button type="button" @click="fillDemoData" 
              class="text-sm font-bold text-brand border-2 border-brand bg-transparent hover:bg-brand/10 px-5 py-2 rounded-full transition-all shadow-sm flex items-center gap-2 tracking-wide mt-4 sm:mt-0 relative top-1">
              <svg class="w-4 h-4 hidden sm:block" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
              FILL DEMO
            </button>
          </div>

          <form @submit.prevent="handleRegister" novalidate class="space-y-8">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
              <!-- Column 1: Core Details (Shared) -->
              <div class="space-y-6">
                <div>
                  <label for="fullName" class="block text-sm font-bold text-content mb-2 tracking-wide">Full Name</label>
                  <input type="text" id="fullName" v-model="formData.fullName"
                    class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:bg-white focus:outline-none focus:ring-[3px] focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all duration-200 placeholder:text-slate-400 text-content "
                    :class="{'border-red-400 focus:border-red-500 bg-red-50/30': errors.fullName}"
                    placeholder="Enter your full name" />
                  <p v-if="errors.fullName" class="text-red-500 text-sm mt-2 flex items-center gap-1 font-bold">{{ errors.fullName }}</p>
                </div>
                
                <div>
                  <label for="email" class="block text-sm font-bold text-content mb-2 tracking-wide">Email Address</label>
                  <input type="email" id="email" v-model="formData.email"
                    class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:bg-white focus:outline-none focus:ring-[3px] focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all duration-200 placeholder:text-slate-400 text-content "
                    :class="{'border-red-400 focus:border-red-500 bg-red-50/30': errors.email}"
                    placeholder="user@university.edu" />
                  <p v-if="errors.email" class="text-red-500 text-sm mt-2 flex items-center gap-1 font-bold">{{ errors.email }}</p>
                </div>

                <div>
                  <label for="password" class="block text-sm font-bold text-content mb-2 tracking-wide">Password</label>
                  <div class="relative">
                    <input :type="showPassword ? 'text' : 'password'" id="password" v-model="formData.password"
                      class="w-full px-4 py-3.5 pr-12 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:bg-white focus:outline-none focus:ring-[3px] focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all duration-200 placeholder:text-slate-400 text-content "
                      :class="{'border-red-400 focus:border-red-500 bg-red-50/30': errors.password}"
                      placeholder="Create a strong password" />
                    <button type="button" @click="showPassword = !showPassword" class="absolute right-4 top-[14px] text-slate-400 hover:text-slate-800 transition-colors focus:outline-none">
                      <svg v-if="!showPassword" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                      <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"></path></svg>
                    </button>
                  </div>
                  <p v-if="errors.password" class="text-red-500 text-sm mt-2 flex items-center gap-1 font-bold">{{ errors.password }}</p>
                </div>

                <div>
                  <div class="flex items-center justify-between mb-2">
                    <label for="nicNumber" class="block text-sm font-bold text-content tracking-wide">NIC Number</label>
                    <span class="text-xs text-slate-400 font-medium">{{ formData.nicNumber.length }}/12</span>
                  </div>
                  <input type="text" id="nicNumber" v-model="formData.nicNumber" maxlength="12"
                    class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:bg-white focus:outline-none focus:ring-[3px] focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all duration-200 placeholder:text-slate-400 text-content "
                    :class="{'border-red-400 focus:border-red-500 bg-red-50/30': errors.nicNumber}"
                    placeholder="e.g. 199912345678 or 991234567V" />
                  <p v-if="errors.nicNumber" class="text-red-500 text-sm mt-2 flex items-center gap-1 font-bold">{{ errors.nicNumber }}</p>
                </div>

                <div>
                  <label for="phoneNumber" class="block text-sm font-bold text-content mb-2 tracking-wide">Phone Number</label>
                  <input type="text" id="phoneNumber" v-model="formData.phoneNumber" maxlength="10"
                    class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:bg-white focus:outline-none focus:ring-[3px] focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all duration-200 placeholder:text-slate-400 text-content "
                    :class="{'border-red-400 focus:border-red-500 bg-red-50/30': errors.phoneNumber}"
                    placeholder="e.g. 0771234567" />
                  <p v-if="errors.phoneNumber" class="text-red-500 text-sm mt-2 flex items-center gap-1 font-bold">{{ errors.phoneNumber }}</p>
                </div>
              </div>

              <!-- Column 2: Role-Specific Details -->
              <div class="space-y-6">
                <!-- === STUDENT FIELDS === -->
                <template v-if="selectedRole === 'STUDENT'">
                  <div>
                    <label for="studentId" class="block text-sm font-bold text-content mb-2 tracking-wide">Student ID</label>
                    <input type="text" id="studentId" v-model="formData.studentId"
                      class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:bg-white focus:outline-none focus:ring-[3px] focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all duration-200 placeholder:text-slate-400 text-content "
                      :class="{'border-red-400 focus:border-red-500 bg-red-50/30': errors.studentId}"
                      placeholder="e.g. IT12345678" />
                    <p v-if="errors.studentId" class="text-red-500 text-sm mt-2 flex items-center gap-1 font-bold">{{ errors.studentId }}</p>
                  </div>

                  <div class="relative">
                    <label for="university" class="block text-sm font-bold text-content mb-2 tracking-wide">University</label>
                    <input type="text" id="university" v-model="universitySearchQuery" 
                      @input="onUniversityInput" @focus="isUniversityDropdownOpen = true" @blur="setTimeout(() => isUniversityDropdownOpen = false, 200)"
                      autocomplete="off"
                      class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:bg-white focus:outline-none focus:ring-[3px] focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all duration-200 placeholder:text-slate-400 text-content "
                      :class="{'border-red-400 focus:border-red-500 bg-red-50/30': errors.university}"
                      placeholder="Search University..." />
                    
                    <ul v-if="isUniversityDropdownOpen" class="absolute z-50 w-full mt-2 bg-white border border-slate-100 rounded-xl shadow-[0_10px_40px_rgba(0,0,0,0.1)] max-h-64 overflow-y-auto">
                      <li v-for="uni in filteredUniversities" :key="uni" 
                        @mousedown="selectUniversity(uni)" 
                        class="px-4 py-3 hover:bg-slate-50 cursor-pointer text-content transition-colors border-b border-slate-50 last:border-0">{{ uni }}</li>
                      <li v-if="filteredUniversities.length === 0" class="px-4 py-3 text-slate-400 text-center">No universities found</li>
                    </ul>
                    <p v-if="errors.university" class="text-red-500 text-sm mt-2 flex items-center gap-1 font-bold">{{ errors.university }}</p>
                  </div>

                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                      <label for="faculty" class="block text-sm font-bold text-content mb-2 tracking-wide">Faculty</label>
                      <select id="faculty" v-model="formData.faculty" @change="onFacultyChange" :disabled="!formData.university"
                        class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:bg-white focus:outline-none focus:ring-[3px] focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all duration-200 appearance-none text-content disabled:opacity-60 disabled:bg-slate-50"
                        :class="{'border-red-400 focus:border-red-500 bg-red-50/30': errors.faculty}">
                        <option value="" disabled>Select Faculty</option>
                        <option v-for="fac in availableFaculties" :key="fac" :value="fac">{{ fac }}</option>
                      </select>
                      <p v-if="errors.faculty" class="text-red-500 text-sm mt-2 font-bold">{{ errors.faculty }}</p>
                    </div>

                    <div>
                      <label for="academicStream" class="block text-sm font-bold text-content mb-2 tracking-wide">Academic Stream</label>
                      <select id="academicStream" v-model="formData.academicStream" :disabled="!formData.faculty"
                        class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:bg-white focus:outline-none focus:ring-[3px] focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all duration-200 appearance-none text-content disabled:opacity-60 disabled:bg-slate-50"
                        :class="{'border-red-400 focus:border-red-500 bg-red-50/30': errors.academicStream}">
                        <option value="" disabled>Select Stream</option>
                        <option v-for="stream in availableStreams" :key="stream" :value="stream">{{ stream }}</option>
                      </select>
                      <p v-if="errors.academicStream" class="text-red-500 text-sm mt-2 font-bold">{{ errors.academicStream }}</p>
                    </div>
                  </div>

                  <div>
                    <label for="academicYear" class="block text-sm font-bold text-content mb-2 tracking-wide">Academic Year</label>
                    <select id="academicYear" v-model="formData.academicYear"
                      class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:bg-white focus:outline-none focus:ring-[3px] focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all duration-200 appearance-none text-content "
                      :class="{'border-red-400 focus:border-red-500 bg-red-50/30': errors.academicYear}">
                      <option value="" disabled>Select Year</option>
                      <option value="Year 1">Year 1</option>
                      <option value="Year 2">Year 2</option>
                      <option value="Year 3">Year 3</option>
                      <option value="Year 4">Year 4</option>
                    </select>
                    <p v-if="errors.academicYear" class="text-red-500 text-sm mt-2 font-bold">{{ errors.academicYear }}</p>
                  </div>
                </template>

                <!-- === LECTURER FIELDS === -->
                <template v-if="selectedRole === 'LECTURER'">
                  <div>
                    <label for="lecturerInstitution" class="block text-sm font-bold text-content mb-2 tracking-wide">University / Institution</label>
                    <input type="text" id="lecturerInstitution" v-model="formData.lecturerInstitution"
                      class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:bg-white focus:outline-none focus:ring-[3px] focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all duration-200 placeholder:text-slate-400 text-content "
                      :class="{'border-red-400': errors.lecturerInstitution}"
                      placeholder="e.g. SLIIT" />
                    <p v-if="errors.lecturerInstitution" class="text-red-500 text-sm mt-2 font-bold">{{ errors.lecturerInstitution }}</p>
                  </div>

                  <div>
                    <label for="lecturerDepartment" class="block text-sm font-bold text-content mb-2 tracking-wide">Department</label>
                    <input type="text" id="lecturerDepartment" v-model="formData.lecturerDepartment"
                      class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:bg-white focus:outline-none focus:ring-[3px] focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all duration-200 placeholder:text-slate-400 text-content "
                      :class="{'border-red-400': errors.lecturerDepartment}"
                      placeholder="e.g. Software Engineering" />
                    <p v-if="errors.lecturerDepartment" class="text-red-500 text-sm mt-2 font-bold">{{ errors.lecturerDepartment }}</p>
                  </div>

                  <div>
                    <label for="lecturerDesignation" class="block text-sm font-bold text-content mb-2 tracking-wide">Designation</label>
                    <input type="text" id="lecturerDesignation" v-model="formData.lecturerDesignation"
                      class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:bg-white focus:outline-none focus:ring-[3px] focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all duration-200 placeholder:text-slate-400 text-content "
                      :class="{'border-red-400': errors.lecturerDesignation}"
                      placeholder="e.g. Senior Lecturer" />
                    <p v-if="errors.lecturerDesignation" class="text-red-500 text-sm mt-2 font-bold">{{ errors.lecturerDesignation }}</p>
                  </div>
                </template>

                <!-- === STAFF FIELDS === -->
                <template v-if="selectedRole === 'STAFF'">
                  <div>
                    <label for="staffDepartment" class="block text-sm font-bold text-content mb-2 tracking-wide">Staff Department</label>
                    <input type="text" id="staffDepartment" v-model="formData.staffDepartment"
                      class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:bg-white focus:outline-none focus:ring-[3px] focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all duration-200 placeholder:text-slate-400 text-content "
                      :class="{'border-red-400': errors.staffDepartment}"
                      placeholder="e.g. Administration" />
                    <p v-if="errors.staffDepartment" class="text-red-500 text-sm mt-2 font-bold">{{ errors.staffDepartment }}</p>
                  </div>

                  <div>
                    <label for="staffId" class="block text-sm font-bold text-content mb-2 tracking-wide">Staff Role / ID</label>
                    <input type="text" id="staffId" v-model="formData.staffId"
                      class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:bg-white focus:outline-none focus:ring-[3px] focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all duration-200 placeholder:text-slate-400 text-content "
                      :class="{'border-red-400': errors.staffId}"
                      placeholder="e.g. Admin / STF993" />
                    <p v-if="errors.staffId" class="text-red-500 text-sm mt-2 font-bold">{{ errors.staffId }}</p>
                  </div>
                </template>
              </div>

              <!-- === ATTACHMENTS LAYER === -->
              <div class="md:col-span-2">
                <!-- STUDENT PHOTO UPLOAD -->
                <div v-if="selectedRole === 'STUDENT'">
                  <label class="block text-sm font-bold text-content mb-2 tracking-wide">Student ID Photo</label>
                  <div class="flex items-center gap-4">
                    <div class="relative flex-1 flex items-center cursor-pointer transition-opacity" @click="triggerFileInput" :class="{'opacity-80': formData.idPhotoPreview}">
                      <input type="file" ref="fileInputRef" @change="onFileChange" accept="image/jpeg, image/png" class="hidden" />
                      <input type="text" :value="formData.idPhoto ? formData.idPhoto.name : ''" readonly placeholder="Choose a file..." 
                        class="w-full px-4 py-3.5 pr-[110px] rounded-xl border-[1.5px] border-[#97C4C4]/50 bg-white hover:border-[#97C4C4] text-content cursor-pointer" />
                      <button type="button" @click.stop="triggerFileInput" class="absolute right-[5px] top-[5px] bottom-[5px] bg-hero-highlight hover:bg-hero-highlight/90 text-white font-bold px-6 rounded-lg pointer-events-none">Browse</button>
                    </div>
                    <div v-if="formData.idPhotoPreview" class="relative shrink-0 w-[60px] h-[60px]">
                      <div class="w-full h-full rounded-xl overflow-hidden shadow-sm"><img :src="formData.idPhotoPreview" class="w-full h-full object-cover" /></div>
                      <button type="button" @click.stop="removePhoto" class="absolute -top-1.5 -right-1.5 bg-hero-highlight text-white w-5 h-5 rounded-full flex items-center justify-center border-2 border-white"><svg class="w-2.5 h-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M6 18L18 6M6 6l12 12"></path></svg></button>
                    </div>
                  </div>
                  
                  <!-- Peer Tutor Toggle -->
                  <div class="mt-8 bg-[#97C4C4]/10 p-5 rounded-xl border border-[#97C4C4]/30">
                    <label class="flex items-center cursor-pointer justify-between w-full">
                      <div class="font-bold text-content tracking-wide flex items-center gap-3">
                        <svg class="w-5 h-5 text-hero-highlight" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path></svg>
                        I want to be a Peer Tutor (Kuppi Teacher)
                      </div>
                      <div class="relative">
                        <input type="checkbox" v-model="formData.isPeerTutor" class="sr-only">
                        <div class="block w-14 h-8 rounded-full transition-colors duration-300" :class="formData.isPeerTutor ? 'bg-hero-highlight' : 'bg-slate-300'"></div>
                        <div class="dot absolute left-1 top-1 bg-white w-6 h-6 rounded-full transition-transform duration-300 shadow-sm" :class="{'translate-x-6': formData.isPeerTutor}"></div>
                      </div>
                    </label>
                  </div>
                </div>

                <!-- LECTURER DOC UPLOAD -->
                <div v-if="selectedRole === 'LECTURER'">
                  <label class="block text-sm font-bold text-content mb-2 tracking-wide">Verification Document / Employee ID</label>
                  <div class="flex items-center gap-4">
                    <div class="relative flex-1 flex items-center cursor-pointer transition-opacity" @click="triggerDocInput">
                      <input type="file" ref="docInputRef" @change="onDocChange" accept=".pdf,image/*" class="hidden" />
                      <input type="text" :value="formData.lecturerDocPreview || ''" readonly placeholder="Upload ID or Letter..." 
                        class="w-full px-4 py-3.5 pr-[110px] rounded-xl border-[1.5px] border-[#97C4C4]/50 bg-white hover:border-[#97C4C4] text-content cursor-pointer" />
                      <button type="button" @click.stop="triggerDocInput" class="absolute right-[5px] top-[5px] bottom-[5px] bg-hero-highlight hover:bg-hero-highlight/90 text-white font-bold px-6 rounded-lg pointer-events-none">Browse</button>
                    </div>
                    <div v-if="formData.lecturerDocPreview" class="relative shrink-0 flex items-center justify-center">
                      <button type="button" @click.stop="removeDoc" class="bg-red-500 hover:bg-red-600 px-4 py-3 rounded-xl text-white font-bold transition-all text-sm shadow-sm">Remove</button>
                    </div>
                  </div>
                  <p class="text-xs text-slate-500 mt-2 ">Please upload a valid PDF, JPG, or PNG (Max 5MB).</p>
                </div>
              </div>
            </div>

            <!-- Global Submit -->
            <div class="mt-10 border-t border-slate-100 pt-8">
              <button type="submit" :disabled="isLoading"
                class="w-full bg-hero-highlight hover:bg-hero-highlight/90 text-white font-bold py-4 px-8 rounded-full transition-all duration-200 transform hover:-translate-y-0.5 shadow-lg shadow-hero-highlight/30 disabled:opacity-70 disabled:cursor-not-allowed disabled:transform-none flex items-center justify-center space-x-2 tracking-wide text-[1.1rem]">
                <svg v-if="isLoading" class="animate-spin -ml-1 mr-2 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                <span>{{ isLoading ? 'CREATING ACCOUNT...' : 'REGISTER' }}</span>
              </button>
            </div>
          </form>
        </div>
      </div>
    </main>
  </div>
</template>
