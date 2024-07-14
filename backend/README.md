### Django Hybrid Architecture

* Monolith Architecture
* Service-Oriented Architecture (SOA): 
Each context exposes its functionality through services.

* DI-Container
* CQRS

* UnitOfWork
* Repository

* AggregateRoot as Model
* Entity as Model


### Remember

* Single app project because of migration foreign key problems when large project?

* Use only coupled settings in config for django features, if you have 
independent infrastructure module like Redis Recommendation System then 
use local config?

* Validation:
    - Django - form.is_valid() or model.full_clean()?
    - DRF - serializer.is_valid() or model.full_clean()?
    - FastAPI - Pydantic auto validation, session.add(item) - auto validation?
