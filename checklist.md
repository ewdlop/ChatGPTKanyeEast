# Checklist

## To ensure the YAML workflow file works perfectly for compiling Python scripts into executables across different platforms, follow these steps:

---

### **Steps to Test and Verify**

#### **1. Double-check File Placement**

- Ensure the YAML file is located in `.github/workflows/`.
- The file should be named appropriately (e.g., `build-python-executable.yml`).

#### **2. Review Your Python Script**

- Make sure your Python script (`your_script.py`) is in the repository's root or the correct relative path defined in the workflow.
- Verify it works locally with PyInstaller:

  ```bash
  pip install pyinstaller
  pyinstaller --onefile your_script.py
  ```

#### **3. Push the Workflow to GitHub**

- Commit and push the workflow YAML file to your repository:

  ```bash
  git add .github/workflows/build-python-executable.yml
  git commit -m "Add workflow to compile Python script to executables"
  git push origin main
  ```

#### **4. Monitor the Workflow Run**

- Go to the **Actions** tab in your GitHub repository to view the running workflow.

#### **5. Debug Common Issues**

If something goes wrong, here are common areas to check:

- **Missing Python Script**:
  Ensure `your_script.py` exists and is in the right path.

- **PyInstaller Errors**:
  If PyInstaller fails (e.g., missing dependencies), add a step in the YAML to install required dependencies:

  ```yaml
  - name: Install dependencies
    run: pip install -r requirements.txt
  ```

- **Workflow Permissions**:
  Ensure the repository has GitHub Actions enabled, and your workflow file uses the correct syntax.

#### **6. Test Artifact Uploads**

- Ensure the artifacts (compiled executables) are uploaded properly:
  - Check the **Actions** tab for artifacts after the workflow run.
  - Download and test the executables.

#### **7. Test Releases**

- If you added the release step, verify:
  - A release is created under the **Releases** section.
  - The executables are attached as assets.
  - Test downloading and running the executables from the release.

---

### **Debugging Tips**

#### **Issue: Workflow Fails**

- Review the logs in the **Actions** tab for error messages.
- Fix any missing dependencies or incorrect paths.

#### **Issue: Missing Executable**

- Ensure `pyinstaller --onefile your_script.py` works locally first.
- Check the `dist/` folder for the expected file after compilation.

---

### Final Verification Checklist

1. The workflow triggers on **push** or **pull requests** to the main branch.
2. Executables are successfully compiled for all platforms.
3. Artifacts are uploaded and can be downloaded from the **Actions** tab.
4. Releases (if enabled) include all executables as downloadable assets.

---

If you encounter any issues during testing, let me know, and I’ll help troubleshoot! 🚀