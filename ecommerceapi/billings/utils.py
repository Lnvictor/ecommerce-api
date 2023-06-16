from datetime import datetime

import requests

from ecommerceapi import settings


__ITAU_HEADERS = {"x-itau-apikey": "123"}
ACCESS_TOKEN_EXPIRES_IN = 300  # seconds


def __generate_itau_access_token() -> str:
    if "x-sandbox-token" in __ITAU_HEADERS.keys():
        time_diff = datetime.now() - datetime.fromisoformat(
            __ITAU_HEADERS.get("access_token_created_at")
        )
        if time_diff.total_seconds() <= ACCESS_TOKEN_EXPIRES_IN:
            return

    payload = {
        "client_id": settings.ITAU_API_CLIENT_ID,
        "client_secret": settings.ITAU_API_CLIENT_SECRET,
    }
    url = f"{settings.ITAU_API_BASE_URL}/api/jwt"
    response = requests.post(url=url, json=payload)

    __ITAU_HEADERS["x-sandbox-token"] = response.json()["access_token"]
    __ITAU_HEADERS["access_token_created_at"] = datetime.now().isoformat()


def _get_itau_request_headers() -> dict:
    __generate_itau_access_token()
    return __ITAU_HEADERS


def _get_itau_request_payload(cpf: str) -> dict:
    return {
        "beneficiario": {
            "id_beneficiario": "312312312",
            "nome_cobranca": "Victor Henrique Barbosa Pereira",
            "tipo_pessoa": {
                "codigo_tipo_pessoa": "F",
                "numero_cadastro_pessoa_fisica": "47185798809",
            },
            "endereco": {
                "nome_logradouro": "rua dona ana neri, 368",
                "nome_bairro": "Mooca",
                "nome_cidade": "Sao Paulo",
                "sigla_UF": "SP",
                "numero_CEP": "12345678",
            },
        },
        "dado_boleto": {
            "descricao_instrumento_cobranca": "boleto",
            "tipo_boleto": "proposta",
            "forma_envio": "impressão",
            "quantidade_parcelas": 2,
            "protesto": {
                "codigo_tipo_protesto": 1,
                "quantidade_dias_protesto": 1,
                "protesto_falimentar": True,
            },
            "negativacao": {
                "codigo_tipo_negativacao": 1,
                "quantidade_dias_negativacao": 1,
            },
            "instrucao_cobranca": [
                {
                    "codigo_instrucao_cobranca": 2,
                    "quantidade_dias_instrucao_cobranca": 10,
                    "dia_util": True,
                }
            ],
            "pagador": {
                "id_pagador": "298AFB64-F607-454E-8FC9-4765B70B7828",
                "pessoa": {
                    "nome_pessoa": "Antônio Coutinho",
                    "nome_fantasia": "Empresa A",
                    "tipo_pessoa": {
                        "codigo_tipo_pessoa": "J",
                        "numero_cadastro_pessoa_fisica": "12345678901",
                        "numero_cadastro_nacional_pessoa_juridica": "12345678901234",
                    },
                },
                "endereco": {
                    "nome_logradouro": "rua dona ana neri, 368",
                    "nome_bairro": "Mooca",
                    "nome_cidade": "Sao Paulo",
                    "sigla_UF": "SP",
                    "numero_CEP": "12345678",
                },
                "texto_endereco_email": "itau@itau-unibanco.com.br",
                "numero_ddd": "011",
                "numero_telefone": "27338668",
                "data_hora_inclusao_alteracao": "2016-02-28T16:41:41.090Z",
            },
            "sacador_avalista": {
                "pessoa": {
                    "nome_pessoa": "Antônio Coutinho",
                    "nome_fantasia": "Empresa A",
                    "tipo_pessoa": {
                        "codigo_tipo_pessoa": "J",
                        "numero_cadastro_pessoa_fisica": "12345678901",
                        "numero_cadastro_nacional_pessoa_juridica": "12345678901234",
                    },
                },
                "endereco": {
                    "nome_logradouro": "rua dona ana neri, 368",
                    "nome_bairro": "Mooca",
                    "nome_cidade": "Sao Paulo",
                    "sigla_UF": "SP",
                    "numero_CEP": "12345678",
                },
                "exclusao_sacador_avalista": True,
            },
            "codigo_carteira": "112",
            "codigo_tipo_vencimento": 1,
            "valor_total_titulo": "580.00",
            "dados_individuais_boleto": [
                {
                    "id_boleto_individual": "b1ff5cc0-8a9c-497e-b983-738904c23389",
                    "status_boleto": "Simulação Solicitada",
                    "situacao_geral_boleto": "Em Aberto",
                    "status_vencimento": "a vencer",
                    "mensagem_status_retorno": "Data vencimento inválida",
                    "numero_nosso_numero": "12345678",
                    "dac_titulo": "1",
                    "data_vencimento": "2000-01-01",
                    "valor_titulo": "180.00",
                    "texto_seu_numero": "123",
                    "codigo_barras": "34101234567890123456789012345678901234567890",
                    "numero_linha_digitavel": "34101234567890123456789012345678901234567890123",
                    "data_limite_pagamento": "2000-01-01",
                    "mensagens_cobranca": [
                        {
                            "mensagem": "conceder desconto de R$ 10,00 até a data de vencimento"
                        }
                    ],
                    "texto_uso_beneficiario": "abc123abc123abc123",
                }
            ],
            "codigo_especie": "01",
            "descricao_especie": "BDP Boleto proposta",
            "codigo_aceite": "S",
            "data_emissao": "2000-01-01",
            "acoes_permitidas": {
                "emitir_segunda_via": True,
                "comandar_instrucao_alterar_dados_cobranca": True,
            },
        },
    }
