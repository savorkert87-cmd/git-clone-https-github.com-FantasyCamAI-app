# Guide de Contribution

Merci de votre intérêt pour FantasyCamAI ! Ce document fournit des directives et des instructions pour contribuer au projet.

## Code de Conduite

En participant à ce projet, vous acceptez de maintenir un environnement respectueux et inclusif.

## Comment Contribuer

### 1. Signaler des Bugs

Avant de créer une issue, vérifiez que le bug n'a pas déjà été signalé. Si vous trouvez un bug :

- Utilisez un titre clair et descriptif
- Décrivez les étapes exactes pour reproduire le problème
- Fournissez des exemples spécifiques
- Décrivez le comportement observé et le comportement attendu
- Incluez des captures d'écran si possible

### 2. Suggérer des Améliorations

Les suggestions sont les bienvenues ! Pour suggérer une amélioration :

- Utilisez un titre clair et descriptif
- Fournissez une description détaillée de l'amélioration suggérée
- Énumérez les exemples spécifiques pour montrer l'utilisation
- Décrivez le comportement actuel et le comportement suggéré

### 3. Pull Requests

Suivez ce processus pour contribuer du code :

1. **Fork** le repository
2. **Créer une branche** avec un nom descriptif
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** vos changements
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push** vers la branche
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Ouvrir une Pull Request** avec une description claire

## Standards de Code

### Python
- Suivez [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Utilisez `black` pour la formatage
- Utilisez `flake8` pour la vérification
- Documentez vos fonctions avec des docstrings

```python
def calculate_video_duration(video_path: str) -> float:
    """
    Calculate the duration of a video file.
    
    Args:
        video_path: Path to the video file
        
    Returns:
        Duration in seconds
    """
```

### JavaScript/TypeScript
- Utilisez `prettier` pour la formatage
- Utilisez `eslint` pour la vérification
- Ecrivez des composants fonctionnels avec React Hooks
- Documentez avec des commentaires JSDoc

```javascript
/**
 * Upload a video file to the server
 * @param {File} file - The video file to upload
 * @returns {Promise<Object>} Response from the server
 */
async function uploadVideo(file) {
  // Implementation
}
```

## Tests

- Écrivez des tests pour toutes les nouvelles fonctionnalités
- Assurez-vous que tous les tests passent avant de soumettre
- Maintenez une couverture de test > 80%

```bash
# Python
pytest --cov=app tests/

# JavaScript
npm test -- --coverage
```

## Documentation

- Mettez à jour le README si nécessaire
- Ajoutez des commentaires pour le code complexe
- Documentez les nouvelles dépendances
- Mettez à jour la documentation API

## Processus de Review

Tous les PR sont examinés par au moins un mainteneur. Nous recherchons :

- Code de qualité et testable
- Respect des standards du projet
- Documentation appropriée
- Pas de dépendances inutiles
- Pas de breaking changes

## Configuration de Développement

```bash
# Backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend Web
cd web
npm install

# Mobile
cd mobile
npm install
```

## Support

- **Issues** : Pour les bugs et les demandes de fonctionnalités
- **Discussions** : Pour les questions et les conversations générales
- **Email** : Pour les questions de sécurité critiques

---

Merci de contribuer à FantasyCamAI ! 🚀
