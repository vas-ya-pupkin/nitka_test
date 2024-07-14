from sqlalchemy.orm import Session

from nitka.app import models, schemas


def get_config(db: Session, config_name: str) -> models.Config | None:
    return db.query(models.Config).filter(models.Config.name == config_name).first()


def create_config(db: Session, config: schemas.Config) -> models.Config:
    db_config = models.Config(
        name=config.name,
        service_config=config.service_config,
        source_tables=config.source_tables,
        target_tables=config.target_tables,
    )
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config
