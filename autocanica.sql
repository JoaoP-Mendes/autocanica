-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 17/06/2026 às 19:00
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `autocanica`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `adm`
--

CREATE TABLE `adm` (
  `email` varchar(30) NOT NULL,
  `senha` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `adm`
--

INSERT INTO `adm` (`email`, `senha`) VALUES
('adm1@email.com', 1234);

-- --------------------------------------------------------

--
-- Estrutura para tabela `carros`
--

CREATE TABLE `carros` (
  `id` int(11) NOT NULL,
  `cpf_cliente` varchar(14) NOT NULL,
  `placa` varchar(10) NOT NULL,
  `marca` varchar(50) DEFAULT NULL,
  `ano` varchar(4) DEFAULT NULL,
  `modelo` varchar(100) DEFAULT NULL,
  `cor` varchar(50) DEFAULT NULL,
  `combustivel` varchar(20) DEFAULT NULL,
  `km_atual` varchar(20) DEFAULT NULL,
  `observacoes` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `carros`
--

INSERT INTO `carros` (`id`, `cpf_cliente`, `placa`, `marca`, `ano`, `modelo`, `cor`, `combustivel`, `km_atual`, `observacoes`) VALUES
(1, '111.222.333-44', 'ABC1D23', 'Fiat', '2018', 'Argo', 'Branco', 'Flex', '45000', ''),
(2, '222.333.444-55', 'XYZ9E87', 'Chevrolet', '2020', 'Onix', 'Preto', 'Flex', '22000', ''),
(3, '333.444.555-66', 'QWE4R56', 'Honda', '2015', 'Civic', 'Cinza', 'Flex', '78000', 'Revisão atrasada');

-- --------------------------------------------------------

--
-- Estrutura para tabela `clientes`
--

CREATE TABLE `clientes` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cpf` varchar(14) NOT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `cep` varchar(10) DEFAULT NULL,
  `cidade` varchar(100) DEFAULT NULL,
  `status` varchar(10) DEFAULT 'Ativo',
  `observacoes` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `clientes`
--

INSERT INTO `clientes` (`id`, `nome`, `cpf`, `telefone`, `email`, `cep`, `cidade`, `status`, `observacoes`) VALUES
(5, 'João Silva', '111.222.333-44', '(67) 99111-2222', 'joao.silva@email.com', '79000-000', 'Campo Grande', 'Ativo', ''),
(6, 'Maria Oliveira', '222.333.444-55', '(67) 99222-3333', 'maria.oliveira@email.com', '79001-000', 'Campo Grande', 'Ativo', ''),
(7, 'Carlos Souza', '333.444.555-66', '(67) 99333-4444', 'carlos.souza@email.com', '79002-000', 'Dourados', 'Inativo', 'Cliente antigo');

-- --------------------------------------------------------

--
-- Estrutura para tabela `ordemservico`
--

CREATE TABLE `ordemservico` (
  `id` int(11) NOT NULL,
  `cpf_cliente` varchar(14) NOT NULL,
  `placa_veiculo` varchar(10) NOT NULL,
  `problema_relatado` varchar(255) DEFAULT NULL,
  `servicos` varchar(255) DEFAULT NULL,
  `data_entrada` date DEFAULT NULL,
  `previsao_entrega` date DEFAULT NULL,
  `valor_total` decimal(10,2) DEFAULT 0.00,
  `status` varchar(20) DEFAULT 'Aberta'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `ordemservico`
--

INSERT INTO `ordemservico` (`id`, `cpf_cliente`, `placa_veiculo`, `problema_relatado`, `servicos`, `data_entrada`, `previsao_entrega`, `valor_total`, `status`) VALUES
(1, '111.222.333-44', 'ABC1D23', 'Ruído ao frear', 'Troca de óleo, Revisão freios', '2026-06-10', '2026-06-12', 280.00, 'Em execucao'),
(2, '222.333.444-55', 'XYZ9E87', 'Carro puxando para o lado', 'Alinhamento e balanceamento', '2026-06-14', '2026-06-15', 90.00, 'Aberta'),
(3, '333.444.555-66', 'QWE4R56', 'Painel com luzes acesas', 'Revisão elétrica', '2026-06-15', '2026-06-17', 150.00, 'Concluida');

-- --------------------------------------------------------

--
-- Estrutura para tabela `servicos`
--

CREATE TABLE `servicos` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `descricao` varchar(255) DEFAULT NULL,
  `status` varchar(10) DEFAULT 'Ativo',
  `preco` decimal(10,2) NOT NULL,
  `tempo_estimado` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `servicos`
--

INSERT INTO `servicos` (`id`, `nome`, `categoria`, `descricao`, `status`, `preco`, `tempo_estimado`) VALUES
(1, 'Troca de óleo', 'Mecanica', 'Troca de óleo e filtro', 'Ativo', 120.00, '30 min'),
(2, 'Alinhamento e balanceamento', 'Mecanica', 'Alinhamento e balanceamento das 4 rodas', 'Ativo', 90.00, '1 hora'),
(3, 'Revisão elétrica', 'Eletrica', 'Diagnóstico completo do sistema elétrico', 'Ativo', 150.00, '2 horas');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `adm`
--
ALTER TABLE `adm`
  ADD UNIQUE KEY `email` (`email`);

--
-- Índices de tabela `carros`
--
ALTER TABLE `carros`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `placa` (`placa`),
  ADD KEY `cpf_cliente` (`cpf_cliente`);

--
-- Índices de tabela `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cpf` (`cpf`);

--
-- Índices de tabela `ordemservico`
--
ALTER TABLE `ordemservico`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cpf_cliente` (`cpf_cliente`),
  ADD KEY `placa_veiculo` (`placa_veiculo`);

--
-- Índices de tabela `servicos`
--
ALTER TABLE `servicos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `carros`
--
ALTER TABLE `carros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `ordemservico`
--
ALTER TABLE `ordemservico`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `servicos`
--
ALTER TABLE `servicos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `carros`
--
ALTER TABLE `carros`
  ADD CONSTRAINT `carros_ibfk_1` FOREIGN KEY (`cpf_cliente`) REFERENCES `clientes` (`cpf`);

--
-- Restrições para tabelas `ordemservico`
--
ALTER TABLE `ordemservico`
  ADD CONSTRAINT `ordemservico_ibfk_1` FOREIGN KEY (`cpf_cliente`) REFERENCES `clientes` (`cpf`),
  ADD CONSTRAINT `ordemservico_ibfk_2` FOREIGN KEY (`placa_veiculo`) REFERENCES `carros` (`placa`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
