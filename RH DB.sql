Create DataBase RH

Use RH

Create Table tb_DEPARTAMENTO
(
  COD_DEPTO             INT                 IDENTITY            ,
  DEPTO                 VARCHAR(30)         NOT NULL
  
  Constraint    PK_TB_DEP_COD_DEPTO   Primary Key (COD_DEPTO)
)

Insert tb_DEPARTAMENTO
( DEPTO )
Values
( 'Comercial' )     ,
( 'Financeiro' )    ,
( 'Jurídico' )  	,
( 'TI' )	        ,
( 'RH' )


Create Table tb_CARGO
(
	COD_CARGO               int					identity        ,
	CARGO				    varchar(30)			not null        ,
	SALARIO_INIC			money				not null

	Constraint  PK_TB_CAR_COD_CARGO  Primary Key (COD_CARGO)
)

Insert tb_CARGO
( CARGO , SALARIO_INIC )
Values
( 'Estagiário'             , 1500  )  ,
( 'Analista Júnior'        , 2000  )  ,
( 'Gerente de Projetos'    , 12000 )  ,
( 'Diretor de Tecnologia'  , 21000 )  ,
( 'CEO'                    , 52000 )


Create Table tb_EMPREGADO
(
	CODFUN                      int					identity    ,		
	NOME						varchar(50)			not null    ,
	NUM_DEPEND					int					not null    ,
	DATA_NASCIMENTO				date				not null    ,
	COD_DEPTO					int					not null    ,
	COD_CARGO					int					not null    ,
	DATA_ADMISSAO				date				not null    ,
	SALARIO						money				not null    ,
	PREMIO_MENSAL				money				not null    ,
	SINDICALIZADO				char(01)			not null    , -- S: SINDICALIZADO, N: NÃO SINDICALIZADO
	OBS							varchar(300)				    ,
	FOTO						image						    ,
	COD_SUPERVISOR				int

	Constraint	TB_EMP_CODFUN		Primary Key (CODFUN)                                              ,
	Constraint	FK_EMP_COD_DEPTO	Foreign Key (COD_DEPTO)	References TB_DEPARTAMENTO  (COD_DEPTO)   ,
	Constraint	FK_EMP_COD_CARGO	Foreign Key (COD_CARGO)	References TB_CARGO         (COD_CARGO)
)

Insert tb_EMPREGADO
( NOME , NUM_DEPEND , DATA_NASCIMENTO , COD_DEPTO , COD_CARGO , DATA_ADMISSAO , SALARIO , PREMIO_MENSAL , SINDICALIZADO )
VALUES
( 'Ronaldo Assis', 1 , '1980-03-21' , 2 , 5 , '1990-11-20' , 52000 , 15000 , 'S' )


Create Table tb_DEPENDENTE
(
	CODFUN						int					not null,
	CODDEP						int					not null, 
	NOME						varchar(50)			not null,
	DATA_NASCIMENTO				date				not null

	Constraint	PK_TB_DEP_CODDEP		Primary Key (CODDEP)                                        ,
	Constraint	FK_TB_DEP_CODFUN		Foreign Key (CODFUN)	References tb_EMPREGADO (CODFUN)		
)

Insert tb_DEPENDENTE
( CODFUN , CODDEP , NOME , DATA_NASCIMENTO )
VALUES
( 1 , 1002 , 'Marcia Assis' , '2005-11-23' )


Select * From tb_DEPARTAMENTO
Select * From tb_CARGO
Select * From tb_EMPREGADO
Select * From tb_DEPENDENTE
