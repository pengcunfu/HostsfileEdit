<template>
  <div id="app">
    <!-- 导航栏 -->
    <nav class="navbar">
      <div class="container">
        <div class="nav-content">
          <div class="nav-brand">
            <router-link to="/" class="brand-link">
              <div class="brand-icon">H</div>
              <span class="brand-text">Hosts文件编辑工具</span>
            </router-link>
          </div>
          
          <div class="nav-menu" :class="{ active: mobileMenuOpen }">
            <router-link to="/" class="nav-link" @click="closeMobileMenu">首页</router-link>
            <router-link to="/features" class="nav-link" @click="closeMobileMenu">功能特性</router-link>
            <router-link to="/download" class="nav-link" @click="closeMobileMenu">下载</router-link>
          </div>
          
          <button class="mobile-toggle" @click="toggleMobileMenu">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </div>
    </nav>

    <!-- 主要内容 -->
    <main>
      <router-view />
    </main>

    <!-- 页脚 -->
    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-info">
            <h3>Hosts文件编辑工具</h3>
            <p>专业的Windows系统hosts文件管理解决方案</p>
          </div>
          <div class="footer-links">
            <div class="footer-section">
              <h4>产品</h4>
              <router-link to="/features">功能特性</router-link>
              <router-link to="/download">下载安装</router-link>
            </div>
            <div class="footer-section">
              <h4>支持</h4>
              <a href="#" @click.prevent>使用帮助</a>
              <a href="#" @click.prevent>常见问题</a>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <p>&copy; 2025 Hosts文件编辑工具. 保留所有权利.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      mobileMenuOpen: false
    }
  },
  methods: {
    toggleMobileMenu() {
      this.mobileMenuOpen = !this.mobileMenuOpen
    },
    closeMobileMenu() {
      this.mobileMenuOpen = false
    }
  }
}
</script>

<style scoped>
/* 导航栏样式 */
.navbar {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(229, 231, 235, 0.8);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.nav-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 0;
}

.brand-link {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: #1f2937;
}

.brand-icon {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  color: white;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 20px;
}

.brand-text {
  font-size: 20px;
  font-weight: 700;
  color: #1f2937;
}

.nav-menu {
  display: flex;
  gap: 32px;
  align-items: center;
}

.nav-link {
  text-decoration: none;
  color: #4b5563;
  font-weight: 500;
  padding: 8px 16px;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.nav-link:hover,
.nav-link.router-link-active {
  color: #2563eb;
  background: rgba(37, 99, 235, 0.1);
}

.mobile-toggle {
  display: none;
  flex-direction: column;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
  gap: 4px;
}

.mobile-toggle span {
  width: 24px;
  height: 2px;
  background: #4b5563;
  transition: all 0.3s ease;
}

/* 页脚样式 */
.footer {
  background: #1f2937;
  color: white;
  margin-top: 80px;
}

.footer-content {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 48px;
  padding: 48px 0;
}

.footer-info h3 {
  font-size: 24px;
  margin-bottom: 12px;
  color: white;
}

.footer-info p {
  color: #9ca3af;
  font-size: 16px;
}

.footer-links {
  display: flex;
  gap: 48px;
}

.footer-section h4 {
  font-size: 18px;
  margin-bottom: 16px;
  color: white;
}

.footer-section a {
  display: block;
  color: #9ca3af;
  text-decoration: none;
  margin-bottom: 8px;
  transition: color 0.2s ease;
}

.footer-section a:hover {
  color: #60a5fa;
}

.footer-bottom {
  border-top: 1px solid #374151;
  padding: 24px 0;
  text-align: center;
}

.footer-bottom p {
  color: #9ca3af;
  font-size: 14px;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .mobile-toggle {
    display: flex;
  }
  
  .nav-menu {
    position: fixed;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    flex-direction: column;
    padding: 24px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    transform: translateY(-100%);
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
  }
  
  .nav-menu.active {
    transform: translateY(0);
    opacity: 1;
    visibility: visible;
  }
  
  .footer-content {
    grid-template-columns: 1fr;
    gap: 32px;
    text-align: center;
  }
  
  .footer-links {
    justify-content: center;
    gap: 32px;
  }
}
</style>
